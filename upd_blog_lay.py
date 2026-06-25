import os
import re

BLOG_DIR = "./blog"
BLOG_INDEX = "./blogs.html"

# --- HTML templates ---
HEADER = """<header class="site-header">
<div class="container">
<p class="logo"><a href="/index.html">Atkinson IT Ltd</a></p>
<nav>
<div class="brand">
<img src="/logo.svg" alt="Atkinson IT logo" loading="lazy">
<span>Atkinson IT Ltd</span>
</div>
<div class="links">
<a href="/index.html">Home</a>
<a href="/it-services.html">Services</a>
<a href="/engineering-services.html">Engineering Services</a>
<a href="/about.html">About</a>
<a href="/capabilities.html">Capabilities</a>
<a href="/testimonials.html">Testimonials</a>
<a href="/casestudies">Case Studies</a>
<a href="/blogs">Blog</a>
<a href="/index.html#contact">Contact</a>
</div>
</nav>
</div>
</header>
"""

FOOTER = """<footer>
  <p>&copy; 2026 Atkinson IT Ltd — Practical IT support for any organisation</p>
  <p>
    <a href="/index.html">Home</a> |
    <a href="/it-services.html">Services</a> |
    <a href="/engineering-services.html">Engineering Services</a> |
    <a href="/about.html">About</a> |
    <a href="/capabilities.html">Capabilities</a> |
    <a href="/testimonials.html">Testimonials</a> |
    <a href="/casestudies">Case Studies</a> |
    <a href="/blogs">Blog</a> |
    <a href="/privacy.html">Privacy Policy</a>
  </p>
</footer>
"""

def wrap_content(html, title):
    """Wrap blog content in unified container/block layout."""
    # Remove old nav/footer
    html = re.sub(r"<nav[\s\S]*?</nav>", "", html)
    html = re.sub(r"<footer[\s\S]*?</footer>", "", html)
    html = re.sub(r"<!DOCTYPE html>|<html[^>]*>|</html>|<head>[\s\S]*?</head>|<body>|</body>", "", html)

    # Extract main content
    match = re.search(r"(<h1[^>]*>[\s\S]*?</h1>[\s\S]*)", html)
    content = match.group(1) if match else html

    # Build new layout
    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Atkinson IT Ltd</title>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{HEADER}
<main class="container">
<div class="block">
{content}
<p><a href="/blogs" class="button">← Back to Blog Index</a></p>
</div>
</main>
{FOOTER}
</body>
</html>"""
    return new_html

def process_blog_posts():
    for file in os.listdir(BLOG_DIR):
        if not file.endswith(".html"):
            continue
        path = os.path.join(BLOG_DIR, file)
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html)
        title = title_match.group(1).strip() if title_match else file.replace(".html", "")

        updated_html = wrap_content(html, title)

        with open(path, "w", encoding="utf-8") as f:
            f.write(updated_html)

        print(f"✔ Updated blog layout: {file}")

def update_blog_index():
    """Rebuild blogs.html using case-study grid layout."""
    posts = []
    for file in sorted(os.listdir(BLOG_DIR)):
        if not file.endswith(".html"):
            continue
        path = os.path.join(BLOG_DIR, file)
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html)
        title = title_match.group(1).strip() if title_match else file.replace(".html", "")
        posts.append(f"<article class='blog-card'><h3>{title}</h3><p><a class='button' href='/blog/{file}'>Read Post</a></p></article>")

    grid = "\n".join(posts)
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog | Atkinson IT Ltd</title>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{HEADER}
<main class="container">
<h1>Blog</h1>
<p><em>Weekly SME IT updates, deep dives, and practical advice.</em></p>
<section class="blog-grid">
{grid}
</section>
</main>
{FOOTER}
</body>
</html>"""

    with open(BLOG_INDEX, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("✔ Rebuilt blogs.html index")

def main():
    print("🔧 Updating blog layouts...\n")
    process_blog_posts()
    update_blog_index()
    print("\n🎉 Blog system updated successfully!")

if __name__ == "__main__":
    main()
