import os

# Pages and their appropriate meta descriptions
meta_descriptions = {
    "privacy.html": "Read the Atkinson IT Ltd privacy policy, including how we handle data and user information.",
    "testimonials.html": "Client testimonials and feedback about Atkinson IT Ltd’s IT consultancy and engineering services.",
    "blogs.html": "Browse the latest blog posts from Atkinson IT Ltd covering IT, engineering, cloud, and reliability topics.",
    "casestudies.html": "Explore real-world case studies showcasing Atkinson IT Ltd’s engineering, cloud, and infrastructure work.",
    "capabilities.html": "Learn about Atkinson IT Ltd’s technical capabilities across systems engineering, infrastructure, and diagnostics.",
    "about.html": "Discover the background, experience, and engineering-led approach behind Atkinson IT Ltd.",
    "it-services.html": "IT services from Atkinson IT Ltd, including cloud migration, networking, support, and infrastructure reliability."
}

def add_meta_description(filename, description):
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if meta description already exists
    if 'name="description"' in content.lower():
        print(f"✔ Meta description already present in {filename}, skipping")
        return

    # Insert meta description just after <head>
    if "<head>" in content:
        updated = content.replace(
            "<head>",
            f"<head>\n<meta name=\"description\" content=\"{description}\">"
        )
    else:
        print(f"❌ No <head> tag found in {filename}, skipping")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ Added meta description to {filename}")


# Process each page
for file, desc in meta_descriptions.items():
    add_meta_description(file, desc)
