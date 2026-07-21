import sys
import json
from pathlib import Path
from html.parser import HTMLParser

class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_json = False
        self.blocks = []
        self.current = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "script":
            d = dict(attrs)
            if "type" in d and d["type"].lower() == "application/ld+json":
                self.in_json = True
                self.current = []

    def handle_endtag(self, tag):
        if tag.lower() == "script" and self.in_json:
            self.in_json = False
            text = "".join(self.current).strip()
            if text:
                self.blocks.append(text)
            self.current = []

    def handle_data(self, data):
        if self.in_json:
            self.current.append(data)

def extract_blocks(html_text):
    p = Extractor()
    p.feed(html_text)
    return p.blocks

def check_schema(obj):
    errs = []

    if "@context" not in obj:
        errs.append("missing @context")
    if "@type" not in obj:
        errs.append("missing @type")

    t = obj.get("@type")

    if t == "BlogPosting":
        required = ["headline", "description", "datePublished"]
        for f in required:
            if f not in obj:
                errs.append("BlogPosting missing field " + f)

    if t == "FAQPage":
        if "mainEntity" not in obj:
            errs.append("FAQPage missing mainEntity")
        else:
            me = obj["mainEntity"]
            if not isinstance(me, list):
                errs.append("FAQPage mainEntity must be list")
            else:
                for i in range(len(me)):
                    q = me[i]
                    if "@type" not in q or q["@type"] != "Question":
                        errs.append("FAQPage mainEntity item " + str(i) + " must be Question")
                    if "name" not in q:
                        errs.append("FAQPage Question " + str(i) + " missing name")
                    if "acceptedAnswer" not in q:
                        errs.append("FAQPage Question " + str(i) + " missing acceptedAnswer")
                    else:
                        ans = q["acceptedAnswer"]
                        if "@type" not in ans or ans["@type"] != "Answer":
                            errs.append("FAQPage Question " + str(i) + " acceptedAnswer must be Answer")
                        if "text" not in ans:
                            errs.append("FAQPage Question " + str(i) + " Answer missing text")

    return errs

def validate_file(path):
    try:
        html = path.read_text(encoding="utf-8")
    except Exception as e:
        print("Could not read " + str(path) + ": " + str(e))
        return

    blocks = extract_blocks(html)
    if not blocks:
        return

    for i in range(len(blocks)):
        block = blocks[i]
        try:
            obj = json.loads(block)
        except Exception as e:
            print("JSON parse error in " + str(path) + " block " + str(i+1) + ": " + str(e))
            continue

        errs = check_schema(obj)
        if errs:
            print("Schema issues in " + str(path) + " block " + str(i+1) + ":")
            for e in errs:
                print
