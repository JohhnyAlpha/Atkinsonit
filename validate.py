import os
import re
import json

ROOT = "/Users/bernardatkinson/AtkinsonIT"

# Regex to extract JSON-LD blocks
JSONLD_BLOCK = re.compile(
    r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE
)

def validate_file(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    blocks = JSONLD_BLOCK.findall(html)
    if not blocks:
        return None, []  # no JSON-LD

    results = []
    for block in blocks:
        json_text = block.strip()

        try:
            json.loads(json_text)
            results.append(("VALID", None))
        except json.JSONDecodeError as e:
            results.append(("INVALID", str(e)))

    return path, results


def walk():
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                filename, results = validate_file(path)

                if filename is None:
                    continue

                for status, err in results:
                    if status == "VALID":
                        print(f"[VALID]   {filename}")
                    else:
                        print(f"[INVALID] {filename}")
                        print(f"          Error: {err}")


if __name__ == "__main__":
    walk()
    print("JSON-LD validation complete.")
