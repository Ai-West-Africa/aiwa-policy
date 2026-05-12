#!/usr/bin/env python3
"""
Combine all AIWA policy documents into a single markdown file for DOCX/PDF generation.
Usage: python3 combine_policy.py <VERSION> <DATE> <OUTPUT_PATH>
"""

import sys
import os

VERSION = sys.argv[1]
DATE = sys.argv[2]
OUTPUT = sys.argv[3]

# Document order: Governance → Standards → Docs (logical reading order)
DOCS = [
    ("governance/roles-and-responsibilities.md", "AIWA-GOV-01"),
    ("governance/decision-framework.md", "AIWA-GOV-02"),
    ("standards/terminology.md", "AIWA-STD-01"),
    ("standards/definitions.md", "AIWA-STD-02"),
    ("standards/classification-matrix.md", "AIWA-STD-03"),
    (
        "docs/01-cultural-classification/cultural-resource-classification-definitions.md",
        "AIWA-DOC-01",
    ),
    (
        "docs/02-legal-alignment/governing-legal-alignment-structural-reality.md",
        "AIWA-DOC-02",
    ),
    (
        "docs/03-process-procedures/process-and-procedures-for-all-works.md",
        "AIWA-DOC-03",
    ),
]

FRONTMATTER = f"""\
---
title: "AI West Africa — Complete Policy & Governance Framework"
subtitle: "Release {VERSION} · {DATE}"
author: "AI West Africa (AIWA)"
date: "{DATE}"
geometry: "margin=1in"
fontsize: "11pt"
colorlinks: true
toc: true
toc-depth: 3
header-includes: |
  \\usepackage{{fancyhdr}}
  \\pagestyle{{fancy}}
  \\fancyhead[L]{{AI West Africa — Policy Framework}}
  \\fancyhead[R]{{{VERSION}}}
  \\fancyfoot[C]{{\\thepage}}
  \\renewcommand{{\\headrulewidth}}{{0.4pt}}
---

"""

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write(FRONTMATTER)

    for i, (path, doc_id) in enumerate(DOCS):
        full_path = os.path.join(repo_root, path)
        with open(full_path, encoding="utf-8") as f:
            content = f.read().strip()
        out.write(content)
        # Page break between documents (works for both LaTeX/PDF and DOCX)
        out.write("\n\n\\newpage\n\n")

print(f"Combined {len(DOCS)} documents → {OUTPUT}")
