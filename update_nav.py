import os
import re

ROOT = "."

# New navigation block
NEW_NAV = """
<nav>
<div class="brand">
<img src="logo.svg" alt="Atkinson IT logo" loading="lazy">
<span>Atkinson IT Ltd</span>
</div>

<div class="links">
<a href="index.html">Home</a>
<a href="it-services.html">Services</a>
<a href="engineering-services.html">Engineering Services</a>
<a href="about.html">About</a>
<a href="capabilities.html">Capabilities</a>
<a href="testimonials.html">Testimonials</a>
<a href="casestudies">Case Studies</a>
<a href="blogs">Blog</a>
<a href="index.html#contact">Contact</a>
</div>
</nav>
""".strip()

# Regex to match the entire <nav>...</nav> block
NAV_PATTERN = re.compile(
    r"<nav[\s\S]*?</nav>",
    re.IGNORECASE
)

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Replace nav block
    content = NAV_PATTERN.sub(NEW_NAV, content)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated nav in: {path}")

def walk():
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    walk()
    print("All nav bars updated.")
