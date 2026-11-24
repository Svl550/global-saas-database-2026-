"""
Packages the commercial dataset files into a clean distribution ZIP archive.
"""
import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")
ZIP_PATH = os.path.join(BASE_DIR, "global-saas-startups-database-2026.zip")

readme_content = """=============================================================
GLOBAL SAAS & HIGH-GROWTH STARTUPS DATABASE (2026 EDITION)
=============================================================

Thank you for your purchase!

This archive contains the full, verified database of 1,000+ technology
companies, AI startups, and SaaS products in 3 universal formats:

1. global_saas_database_2026.csv
   - Ready for direct import into Microsoft Excel, Google Sheets,
     Airtable, Notion, or CRM tools (HubSpot, Salesforce).
   - Encoded in UTF-8.

2. global_saas_database_2026.json
   - Ideal for developers, API integrations, and web applications.
   - Beautifully formatted and structured.

3. global_saas_database_2026.sqlite
   - Pre-indexed standalone relational database file.
   - Open with DB Browser for SQLite, DBeaver, or directly via Python/Node.js:
     Query example:
     SELECT company_name, website, tech_stack FROM startups WHERE category = 'AI & Machine Learning';

COMMERCIAL LICENSE:
You have full commercial rights to use this data for internal analytics,
marketing, lead generation, consulting, or client deliverables.
Redistribution or public resale of the raw database file is prohibited.

Support / Questions:
Visit our store: https://svl.gumroad.com
=============================================================
"""

# Write license / instructions inside dist
guide_path = os.path.join(DIST_DIR, "QUICKSTART_GUIDE_AND_LICENSE.txt")
with open(guide_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

files_to_pack = [
    ("global_saas_database_2026.csv", os.path.join(DIST_DIR, "global_saas_database_2026.csv")),
    ("global_saas_database_2026.json", os.path.join(DIST_DIR, "global_saas_database_2026.json")),
    ("global_saas_database_2026.sqlite", os.path.join(DIST_DIR, "global_saas_database_2026.sqlite")),
    ("QUICKSTART_GUIDE_AND_LICENSE.txt", guide_path)
]

with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
    for arcname, filepath in files_to_pack:
        if os.path.exists(filepath):
            zipf.write(filepath, arcname=arcname)
            print(f"[+] Added {arcname} ({os.path.getsize(filepath):,} bytes)")

print(f"[SUCCESS] Packaged distribution ZIP: {ZIP_PATH} ({os.path.getsize(ZIP_PATH):,} bytes)")
