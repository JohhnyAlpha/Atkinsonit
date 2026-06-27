import os
from bs4 import BeautifulSoup

CASESTUDY_DIR = "./casestudy"
BACKUP_SUFFIX = ".bak"

HERO_SUBTITLE = "Modernising systems through clear, reliable technical work."

MODERN_HEADER = """
<nav>
<div class="brand">
<img alt="Atkinson IT logo" loading="lazy" src="/logo.svg"/>
<span>Atkinson IT Ltd</span>
</div>
<div class="links">
<a href="/">Home</a>
<a href="/it-services">Services</a>
<a href="/engineering-services">Engineering Services</a>
<a href="/about">About</a>
<a href="/capabilities">Capabilities</a>
<a href="/testimonials">Testimonials</a>
<a href="/casestudies">Case Studies</a>
<a href="/blogs">Blog</a>
<a href="/#contact">Contact</a>
</div>
</nav>
"""

MODERN_FOOTER = """
<footer>
<p>© 2026 Atkinson IT Ltd — Practical IT support for any organisation</p>
<p>
<a href="/">Home</a> |
<a href="/it-services">Services</a> |
<a href="/engineering-services">Engineering Services</a> |
<a href="/about">About</a> |
<a href="/capabilities">Capabilities</a> |
<a href="/testimonials">Testimonials</a> |
<a href="/casestudies">Case Studies</a> |
<a href="/blogs">Blog</a> |
<a href="/privacy">Privacy Policy</a>
</p>
</footer>
"""

def get_related_case_studies(current_filename):
    files = [f for f in os.listdir(CASESTUDY_DIR) if f.endswith(".html")]
    files.remove(current_filename)
    return files

def format_case_study(path):
    print(f"Processing {path}")

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    backup_path = path + BACKUP_SUFFIX
    with open(backup_path, "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    if not body:
        print(f"⚠ No <body> found in {path}, skipping.")
        return

    # Remove old header/footer/nav/breadcrumbs
    for tag in body.find_all(["header", "nav", "footer"]):
        tag.decompose()
    for tag in body.find_all("div", class_="breadcrumbs"):
        tag.decompose()

    # Remove "A case study by Atkinson IT Ltd"
    for em_tag in body.find_all("em"):
        if "case study" in em_tag.get_text().lower():
            em_tag.parent.decompose()

    # Replace <main class="case-study"> with <main class="container">
    main_tag = soup.find("main")
    if main_tag:
        main_tag["class"] = ["container"]

    # Extract hero image
    hero_img = soup.find("img")
    hero_src = hero_img["src"] if hero_img else ""

    # Extract title
    title_tag = soup.find("h1")
    title_text = title_tag.get_text(strip=True) if title_tag else "Case Study"

    # Insert modern header
    header_soup = BeautifulSoup(MODERN_HEADER, "html.parser")
    body.insert(0, header_soup)

    # Insert modern breadcrumbs
    breadcrumbs = BeautifulSoup(f"""
<div class="breadcrumbs">
<a href="/">Home</a> ›
<a href="/casestudies">Case Studies</a> ›
<span>{title_text}</span>
</div>
""", "html.parser")
    body.insert(1, breadcrumbs)

    # Insert hero
    hero_section = BeautifulSoup(f"""
<section class="hero-service">
<div class="container">
<h2>{title_text}</h2>
<p>{HERO_SUBTITLE}</p>
</div>
</section>
""", "html.parser")
    body.insert(2, hero_section)

    # Wrap each <section> in .service-block
    main = soup.find("main")
    if main:
        for section in main.find_all("section"):
            wrapper = soup.new_tag("div", **{"class": "service-block"})
            section.wrap(wrapper)

    # Contact box
    contact_box = BeautifulSoup("""
<section class="service-block">
<h2>Get in Touch</h2>
<p>If you'd like help with a similar project, you can reach us directly through our main contact section.</p>
<p><a class="button" href="/#contact">Go to Contact Us</a></p>
</section>
""", "html.parser")
    body.append(contact_box)

    # Dynamic related case studies
    filename = os.path.basename(path)
    related = get_related_case_studies(filename)

    related_html = "<section class='service-block'><h2>Related Case Studies</h2><ul>"
    for r in related:
        name = r.replace(".html", "").replace("-", " ").title()
        related_html += f"<li><a href='/casestudy/{r}'>{name}</a></li>"
    related_html += "</ul></section>"

    related_block = BeautifulSoup(related_html, "html.parser")
    body.append(related_block)

    # Insert modern footer
    footer_soup = BeautifulSoup(MODERN_FOOTER, "html.parser")
    body.append(footer_soup)

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✔ Updated {path}")

def main():
    for filename in os.listdir(CASESTUDY_DIR):
        if filename.endswith(".html"):
            format_case_study(os.path.join(CASESTUDY_DIR, filename))

if __name__ == "__main__":
    main()
