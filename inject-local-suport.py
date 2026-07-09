import os
import re

ROOT = "."

LOCAL_BLOCK = """
<section class="section">
    <h2>Local IT Support</h2>
    <p>Atkinson IT provides reliable, local IT support across Surrey, Berkshire, Heathrow and the surrounding areas.</p>

    <div class="grid">

        <div class="box">
            <h3>Staines-upon-Thames</h3>
            <p>Local IT support for SMEs, sole traders and growing organisations.</p>
            <p><a href="/it-support-staines" style="font-weight:bold; color:#0A2A43;">IT Support in Staines →</a></p>
        </div>

        <div class="box">
            <h3>Egham</h3>
            <p>Support for businesses near Egham High Street and Royal Holloway.</p>
            <p><a href="/it-support-egham" style="font-weight:bold; color:#0A2A43;">IT Support in Egham →</a></p>
        </div>

        <div class="box">
            <h3>Chertsey</h3>
            <p>Reliable IT support for Chertsey town centre and industrial estates.</p>
            <p><a href="/it-support-chertsey" style="font-weight:bold; color:#0A2A43;">IT Support in Chertsey →</a></p>
        </div>

        <div class="box">
            <h3>Woking</h3>
            <p>Support for Woking businesses, offices and surrounding villages.</p>
            <p><a href="/it-support-woking" style="font-weight:bold; color:#0A2A43;">IT Support in Woking →</a></p>
        </div>

        <div class="box">
            <h3>Windsor</h3>
            <p>Local IT support for Windsor town centre and riverside businesses.</p>
            <p><a href="/it-support-windsor" style="font-weight:bold; color:#0A2A43;">IT Support in Windsor →</a></p>
        </div>

        <div class="box">
            <h3>Slough</h3>
            <p>Support for Slough Trading Estate and surrounding business parks.</p>
            <p><a href="/it-support-slough" style="font-weight:bold; color:#0A2A43;">IT Support in Slough →</a></p>
        </div>

        <div class="box">
            <h3>Heathrow</h3>
            <p>IT support for logistics, aviation-adjacent and cargo businesses.</p>
            <p><a href="/it-support-heathrow" style="font-weight:bold; color:#0A2A43;">IT Support near Heathrow →</a></p>
        </div>

        <div class="box">
            <h3>Surrey</h3>
            <p>Support across Surrey’s business parks, offices and SMEs.</p>
            <p><a href="/it-support-surrey" style="font-weight:bold; color:#0A2A43;">IT Support in Surrey →</a></p>
        </div>

        <div class="box">
            <h3>Berkshire</h3>
            <p>Support across Berkshire including Reading, Maidenhead and Windsor.</p>
            <p><a href="/it-support-berkshire" style="font-weight:bold; color:#0A2A43;">IT Support in Berkshire →</a></p>
        </div>

    </div>

    <p style="margin-top:1.5rem;">
        <a href="/local-it-support" style="font-weight:bold; color:#0A2A43;">View All Local IT Support Areas →</a>
    </p>
</section>
""".strip()

# Detect if block already exists
BLOCK_CHECK = "Local IT Support"

# Insert before Contact section
CONTACT_PATTERN = re.compile(
    r"<section[^>]*id=[\"']contact[\"'][^>]*>",
    re.IGNORECASE
)

def inject_block(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if BLOCK_CHECK in content:
        return  # Already injected

    match = CONTACT_PATTERN.search(content)
    if not match:
        return  # No contact section, skip

    insertion_point = match.start()

    new_content = content[:insertion_point] + LOCAL_BLOCK + "\n\n" + content[insertion_point:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Injected Local IT Support block into: {path}")

def walk():
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".html"):
                inject_block(os.path.join(root, file))

if __name__ == "__main__":
    walk()
    print("Local IT Support block injected into all pages.")
