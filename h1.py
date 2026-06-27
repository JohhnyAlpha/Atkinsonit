import os

# Pages that need an H1 added
pages = {
    "privacy.html": "Privacy Policy",
    "testimonials.html": "Testimonials",
    "blogs.html": "Blog Posts",
    "casestudies.html": "Case Studies",
    "capabilities.html": "Capabilities",
    "about.html": "About Atkinson IT",
    "it-services.html": "IT Services"
}

def add_h1_to_page(filename, h1_text):
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if an H1 already exists
    if "<h1" in content.lower():
        print(f"✔ H1 already present in {filename}, skipping")
        return

    # Insert H1 immediately after <body>
    if "<body>" in content:
        updated = content.replace(
            "<body>",
            f"<body>\n\n<h1>{h1_text}</h1>\n"
        )
    else:
        print(f"❌ No <body> tag found in {filename}, skipping")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ Added H1 to {filename}: {h1_text}")


# Process each page
for file, title in pages.items():
    add_h1_to_page(file, title)
