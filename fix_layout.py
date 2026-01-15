from pathlib import Path
import re

report_path = Path("rapport_etonnement_Tassigny_Pierre_GIL_modern_v2.html")
html = report_path.read_text(encoding="utf-8")

# New CSS patch to fix the layout issues
# 1. .questions-grid: change columns to 1fr (stack vertically)
# 2. .answerbox: change display to block (so paragraphs stack vertically) instead of flex (which was doing row)
layout_fix_css = """
/* Fix Layout V3 : Colonne unique et paragraphes empilés */
.questions-grid {
    grid-template-columns: 1fr !important;
}

.answerbox {
    display: block !important; /* Was flex, caused row layout for paragraphs */
    padding-bottom: 8mm !important; /* Some extra padding for comfort */
}

/* Ensure formatting inside is clean */
.answerbox p {
    display: block !important;
    margin-bottom: 4mm !important;
    text-align: justify;
}
"""

# Append this CSS to the existing <style> block or previously injected patch
# We can just inject it before the closing </style> again, it will override previous rules due to cascade + !important
if "</style>" in html:
    html = html.replace("</style>", layout_fix_css + "\n</style>", 1)
    report_path.write_text(html, encoding="utf-8")
    print("Success: Layout fixed (1-col grid + block paragraphs).")
else:
    print("Error: </style> not found.")
