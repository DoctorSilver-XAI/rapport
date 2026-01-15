from pathlib import Path

report_path = Path("rapport_etonnement_Tassigny_Pierre_GIL_modern_v2.html")
html = report_path.read_text(encoding="utf-8")

# Fix V4: 
# 1. Allows pages to expand vertically (height: auto)
# 2. Removes overflow blocking (overflow: visible)
# 3. Ensures the footer doesn't overlap text (padding-bottom on page)
overflow_fix_css = """
/* Fix Layout V4 : Pages extensibles pour éviter de couper le contenu */
.page {
    height: auto !important;
    min-height: 210mm !important;
    overflow: visible !important;
    padding-bottom: 25mm !important; /* Make space for the footer */
    box-sizing: border-box !important;
}

/* Adjust footer to stay at bottom of the expanded page */
.footer {
    bottom: 8mm !important;
}
"""

if "</style>" in html:
    html = html.replace("</style>", overflow_fix_css + "\n</style>", 1)
    report_path.write_text(html, encoding="utf-8")
    print("Success: Page height set to auto/expandable.")
else:
    print("Error: </style> not found.")
