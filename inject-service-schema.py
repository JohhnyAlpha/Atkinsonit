import os
import re

ROOT = "."

# Mapping of page filenames to their service area names
LOCAL_PAGES = {
    "it-support-staines.html": "Staines-upon-Thames",
    "it-support-egham.html": "Egham",
    "it-support-chertsey.html": "Chertsey",
    "it-support-woking.html": "Woking",
    "it-support-windsor.html": "Windsor",
    "it-support-slough.html": "Slough",
    "it-support-heathrow.html": "Heathrow",
    "it-support-surrey.html": "Surrey",
    "it-support-berkshire.html": "Berkshire"
}

# Detect if schema already exists
SCHEMA_CHECK = "Service"

HEAD_PATTERN = re.compile(r"</head>", re.IGNORECASE)

def generate_schema(area):
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Local IT Support",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Atkinson IT Ltd",
    "url": "https://www.atkinsonit.co.uk",
    "telephone": "+44-7825-261499"
  },
  "areaServed": "%s",
  "description": "Practical, reliable IT support for SMEs, sole traders and organisations in %s."
}
</script>
""" % (area, area)

def inject_schema(path, area):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if SCHEMA_CHECK in content:
        return  # Already injected

    match = HEAD_PATTERN.search(content)
    if not match:
        return  # No head tag found

    schema_block = generate_schema(area)
    insertion_point = match.start()

    new_content = content[:insertion_point] + schema_block + "\n\n" + content[insertion_point:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Injected Service schema into: {path}")

def walk():
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file in LOCAL_PAGES:
                inject_schema(os.path.join(root, file), LOCAL_PAGES[file])

if __name__ == "__main__":
    walk()
    print("Service schema injected into all local IT support pages.")
