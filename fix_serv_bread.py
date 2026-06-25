import os
import re

SERVICE_PATHS = [
    "./it-services.html",
    "./engineering-services.html",
    "./capabilities.html",
]

def move_breadcrumbs_below_hero(html):
    """
    Moves <div class="breadcrumbs"> BELOW the hero block.
    Fixes the double-header issue.
    """

    # Find breadcrumbs
    bc_match = re.search(r'(<div class="breadcrumbs"[\s\S]*?</div>)', html)
    if not bc_match:
        return html

    breadcrumbs = bc_match.group(1)

    # Remove breadcrumbs from current position
    html = html.replace(breadcrumbs, "")

    # Insert breadcrumbs AFTER hero block
    hero_match = re.search(r'(<div class="hero"[\s\S]*?</div>)', html)
    if hero_match:
        hero_block = hero_match.group(1)
        html = html.replace(hero_block, hero_block + "\n" + breadcrumbs)

    return html


def process_file(path):
    if not os.path.exists(path):
        print(f"⚠ Skipped (not found): {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    updated = move_breadcrumbs_below_hero(html)

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✔ Fixed breadcrumb order: {path}")


def main():
    print("🔧 Fixing service breadcrumb order...\n")
    for path in SERVICE_PATHS:
        process_file(path)
    print("\n🎉 Breadcrumb order fixed for all service pages!")


if __name__ == "__main__":
    main()
