#!/usr/bin/env python3
"""
Build script: converts j-make site to static HTML with Schema.org and Open Graph.
Run from the rkg repo root: python3 build.py
"""
import json
import os
import re
import shutil

REPO = "/tmp/rkg"
OUTPUT = os.path.join(REPO, "index.html")
IMAGES_SRC = "/home/richard/Pictures/RKG"
IMAGES_DST = os.path.join(REPO, "images")

# ============================================================
# 1. READ BODY.JSON AND ALL CONTENT FILES
# ============================================================

def read_content(path):
    """Read an index.html content file."""
    full = os.path.join(REPO, "body", path, "index.html")
    if os.path.exists(full):
        with open(full, "r") as f:
            return f.read()
    return ""

def walk_body(arr, parent_path="body"):
    """Walk body.json and collect content for each element."""
    elements = []
    sibling_idx = 0
    for item in arr:
        if isinstance(item, str):
            key = f"{item}_{sibling_idx}"
            path = f"{parent_path}/{key}"
            content = read_content(path)
            elements.append({
                "tag": item,
                "key": key,
                "path": path,
                "content": content,
                "children": []
            })
            sibling_idx += 1
        elif isinstance(item, list):
            # Nested array — children of the last element
            if elements:
                children = walk_body(item, elements[-1]["path"])
                elements[-1]["children"] = children
    return elements

# ============================================================
# 2. BUILD STATIC HTML
# ============================================================

def build_html():
    # Read body.json
    with open(os.path.join(REPO, "body.json"), "r") as f:
        body = json.load(f)

    # Read CSS
    with open(os.path.join(REPO, "style.css"), "r") as f:
        css = f.read()

    # Walk the structure
    elements = walk_body(body)

    # Extract header content
    header_content = ""
    main_article = ""
    main_aside = ""
    sidebar_sections = []
    footer_content = ""

    for el in elements:
        if el["tag"] == "header":
            header_content = el["content"]
        elif el["tag"] == "main":
            for child in el["children"]:
                if child["tag"] == "article":
                    main_article = child["content"]
                elif child["tag"] == "aside":
                    main_aside = child["content"]
                    for sec in child["children"]:
                        sidebar_sections.append(sec["content"])
        elif el["tag"] == "footer":
            footer_content = el["content"]

    # Build sidebar sections HTML
    sidebar_html = main_aside
    for sec in sidebar_sections:
        sidebar_html += f"\n<section>{sec}</section>"

    # ============================================================
    # 3. SCHEMA.ORG JSON-LD
    # ============================================================

    schema_person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Richard Kent Gates",
        "url": "https://richardkentgates.com",
        "image": "https://richardkentgates.com/images/rkg_logo_640x640.jpg",
        "email": "mail@richardkentgates.com",
        "jobTitle": "Developer & Researcher",
        "founder": {
            "@type": "Organization",
            "name": "Gap Creek Media",
            "url": "https://gapcreekmedia.com"
        },
        "sameAs": [
            "https://github.com/richardkentgates"
        ],
        "knowsAbout": [
            "WordPress Development",
            "Theoretical Physics",
            "Cosmology",
            "Scalar Field Theory",
            "Quantum Gravity",
            "Server Provisioning"
        ]
    }

    schema_website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Richard Kent Gates",
        "url": "https://richardkentgates.com",
        "description": "Developer, researcher, and founder of Gap Creek Media. Privacy-first WordPress tools and independent research in theoretical physics.",
        "author": {"@type": "Person", "name": "Richard Kent Gates"},
        "inLanguage": "en"
    }

    # Papers as ScholarlyArticle
    papers = [
        {
            "name": "The Theory of Everything: One Axiom, One Field, All of Physics",
            "url": "https://richardkentgates.com/papers/theory-of-everything.html",
            "description": "One axiom generates quantum mechanics, general relativity, and thermodynamics. One scalar field IS the quantum vacuum, IS spacetime. One correction law bridges GR and QM."
        },
        {
            "name": "Time-Gradient Field Model",
            "url": "https://richardkentgates.com/papers/time-gradient-field-model.html",
            "description": "Unified mathematical explanation for decay-rate and lifetime anomalies via a scalar time-gradient field."
        },
        {
            "name": "The Field Is the Universe: A Unified Proof",
            "url": "https://richardkentgates.com/papers/unified-proof.html",
            "description": "Working backward from the current state, the field drives expansion, radiation, structure, and accelerated expansion."
        },
        {
            "name": "Black Hole Lifecycle: Field-Driven Cosmology",
            "url": "https://richardkentgates.com/papers/blackhole-lifecycle.html",
            "description": "The field drives expansion. Black hole end-states produce gradient-driven clustering."
        },
        {
            "name": "The Foundation: Distance, Time, Information",
            "url": "https://richardkentgates.com/papers/foundation-proof.html",
            "description": "Distance necessitates time. Time is information. Information cannot be lost. Singularities are forbidden."
        }
    ]

    schema_articles = []
    for p in papers:
        schema_articles.append({
            "@context": "https://schema.org",
            "@type": "ScholarlyArticle",
            "name": p["name"],
            "url": p["url"],
            "description": p["description"],
            "author": {"@type": "Person", "name": "Richard Kent Gates"},
            "publisher": {"@type": "Person", "name": "Richard Kent Gates"}
        })

    # Software projects
    software = [
        {
            "name": "Metamanager",
            "url": "https://github.com/richardkentgates/metamanager-plugin",
            "description": "Complete metadata management for WordPress. Schema.org, Open Graph, sitemaps, lossless media compression."
        },
        {
            "name": "MXRoute Mailer",
            "url": "https://github.com/richardkentgates/mxroute-mailer",
            "description": "Routes WordPress email through MXRoute's HTTP API or SMTP."
        },
        {
            "name": "j-make",
            "url": "https://github.com/richardkentgates/j-make",
            "description": "Client-side library that builds pages from JSON. No build step, no back-end."
        }
    ]

    schema_software = []
    for s in software:
        schema_software.append({
            "@context": "https://schema.org",
            "@type": "SoftwareSourceCode",
            "name": s["name"],
            "url": s["url"],
            "description": s["description"],
            "author": {"@type": "Person", "name": "Richard Kent Gates"},
            "codeRepository": s["url"],
            "programmingLanguage": ["PHP", "JavaScript", "Python"]
        })

    # Combine all schemas
    all_schemas = [schema_person, schema_website] + schema_articles + schema_software
    schema_json = json.dumps(all_schemas, indent=2)

    # ============================================================
    # 4. OPEN GRAPH & TWITTER CARD TAGS
    # ============================================================

    og_tags = """
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Richard Kent Gates">
    <meta property="og:title" content="Richard Kent Gates — Developer & Researcher">
    <meta property="og:description" content="Developer, researcher, and founder of Gap Creek Media. Privacy-first WordPress tools and independent research in theoretical physics and cosmology.">
    <meta property="og:url" content="https://richardkentgates.com">
    <meta property="og:image" content="https://richardkentgates.com/images/rkg_logo_640x640.jpg">
    <meta property="og:image:width" content="640">
    <meta property="og:image:height" content="640">
    <meta property="og:image:alt" content="Richard Kent Gates logo">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Richard Kent Gates — Developer & Researcher">
    <meta name="twitter:description" content="Developer, researcher, and founder of Gap Creek Media. Privacy-first WordPress tools and independent research in theoretical physics and cosmology.">
    <meta name="twitter:image" content="https://richardkentgates.com/images/rkg_logo_640x640.jpg">
    <meta name="description" content="Developer, researcher, and founder of Gap Creek Media. Privacy-first WordPress tools and independent research in theoretical physics and cosmology.">
    <link rel="icon" type="image/png" href="images/rkg_logo_64x64_fav.png">
    <link rel="apple-touch-icon" href="images/rkg_logo_300x300.jpg">
    """

    # ============================================================
    # 5. ASSEMBLE FINAL HTML
    # ============================================================

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Richard Kent Gates — Developer & Researcher</title>
    {og_tags}
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
    <style>
{css}
    </style>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <header>
        {header_content}
    </header>
    <main>
        <article>
            {main_article}
        </article>
        <aside>
            {sidebar_html}
        </aside>
    </main>
    <footer>
        {footer_content}
    </footer>
    <script>
        // Collapse toggle
        document.addEventListener('click', function(e) {{
            var trigger = e.target.closest('.collapse-trigger');
            if (trigger) {{
                var body = trigger.nextElementSibling;
                if (body && body.classList.contains('collapse-body')) {{
                    trigger.classList.toggle('open');
                    body.classList.toggle('open');
                }}
            }}
        }});
    </script>
</body>
</html>"""

    return html

# ============================================================
# 6. MAIN
# ============================================================

def main():
    # Copy images (skip if already present)
    if not os.path.exists(IMAGES_DST):
        if os.path.exists(IMAGES_SRC):
            shutil.copytree(IMAGES_SRC, IMAGES_DST)
            print(f"Copied images to {IMAGES_DST}")
        else:
            print(f"Warning: {IMAGES_SRC} not found, skipping image copy")

    # Build static HTML
    html = build_html()

    # Write
    with open(OUTPUT, "w") as f:
        f.write(html)
    print(f"Static HTML written to {OUTPUT}")
    print(f"Size: {len(html)} bytes")

    # Count schemas
    schema_count = html.count('"@type"')
    print(f"Schema.org types: {schema_count}")
    print(f"OG tags: {html.count('og:')}")

if __name__ == "__main__":
    main()
