import os
import re

# Pages to process
pages = [
    "index.html",
    "testimonials.html",
    "capabilities.html",
    "it-services.html",
    "engineering-services.html",
    "blogs.html",
    "casestudies.html"
]

def remove_invalid_jsonld(content):
    """Remove <script type='application/ld+json' src='schema.json'>"""
    pattern = r'<script[^>]*type="application/ld\+json"[^>]*src="schema\.json"[^>]*></script>'
    return re.sub(pattern, "", content, flags=re.IGNORECASE)


def fix_heading_levels(content):
    """Fix h3 following h1 by converting h3 → h2"""
    # Only convert h3 that immediately follow an h1 section
    return re.sub(r"<h3>", "<h2>", content), re.sub(r"</h3>", "</h2>", content)


def fix_section_without_heading(content):
    """
    Convert <section> with no heading into <div>.
    A section must contain h2–h6.
    """
    def replace_section(match):
        block = match.group(0)
        if not re.search(r"<h[2-6]>", block):
            return block.replace("<section", "<div").replace("</section>", "</div>")
        return block

    return re.sub(r"<section[^>]*>.*?</section>", replace_section, content, flags=re.DOTALL)


def process_file(filename):
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Apply fixes
    content = remove_invalid_jsonld(content)
    content = fix_section_without_heading(content)
    content = content.replace("<h3>", "<h2>").replace("</h3>", "</h2>")

    if content != original:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Fixed: {filename}")
    else:
        print(f"✔ No changes needed: {filename}")


# Run fixes
for page in pages:
    process_file(page)
