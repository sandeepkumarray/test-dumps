import os
import hashlib
import argparse
from datetime import datetime

EXCLUDED_DIRS = {'.git', '.vs', 'bin', 'obj', 'node_modules', '__pycache__', '.idea'}

def hash_file(path, block_size=65536):
    """Return SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(block_size), b""):
            h.update(chunk)
    return h.hexdigest()

def collect_files(base_dir):
    """Return dict of relative path → absolute path for all files."""
    file_map = {}
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), base_dir)
            file_map[rel] = os.path.join(root, f)
    return file_map

def compare_projects(original_dir, restored_dir):
    orig_files = collect_files(original_dir)
    rest_files = collect_files(restored_dir)

    orig_set, rest_set = set(orig_files), set(rest_files)

    missing = sorted(orig_set - rest_set)
    extra = sorted(rest_set - orig_set)
    common = sorted(orig_set & rest_set)

    changed = []
    for rel in common:
        if hash_file(orig_files[rel]) != hash_file(rest_files[rel]):
            changed.append(rel)

    return {
        "missing": missing,
        "extra": extra,
        "changed": changed,
        "total_original": len(orig_files),
        "total_restored": len(rest_files),
        "original_dir": original_dir,
        "restored_dir": restored_dir
    }

def generate_html_report(result, output_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Project Comparison Report</title>
<style>
body {{ font-family: Arial, sans-serif; background: #0d1117; color: #e6edf3; margin: 2rem; }}
h1, h2 {{ color: #58a6ff; }}
table {{ border-collapse: collapse; width: 100%; margin-bottom: 2rem; }}
th, td {{ padding: 8px 10px; border: 1px solid #30363d; }}
th {{ background: #21262d; text-align: left; }}
tr:nth-child(even) {{ background: #161b22; }}
code {{ background: #21262d; padding: 2px 4px; border-radius: 4px; }}
.status-ok {{ color: #3fb950; font-weight: bold; }}
.status-warn {{ color: #d29922; font-weight: bold; }}
.status-error {{ color: #f85149; font-weight: bold; }}
summary {{ cursor: pointer; color: #58a6ff; }}
details > summary::-webkit-details-marker {{ display: none; }}
</style>
</head>
<body>
<h1>🧩 Project Comparison Report</h1>
<p><strong>Generated:</strong> {timestamp}</p>
<p><strong>Original:</strong> {result["original_dir"]}<br>
<strong>Restored:</strong> {result["restored_dir"]}</p>

<h2>📊 Summary</h2>
<table>
<tr><th>Metric</th><th>Count</th></tr>
<tr><td>Total Original Files</td><td>{result["total_original"]}</td></tr>
<tr><td>Total Restored Files</td><td>{result["total_restored"]}</td></tr>
<tr><td>Missing Files</td><td class="status-error">{len(result["missing"])}</td></tr>
<tr><td>Extra Files</td><td class="status-warn">{len(result["extra"])}</td></tr>
<tr><td>Changed Files</td><td class="status-warn">{len(result["changed"])}</td></tr>
</table>
"""

    def list_section(title, items, css_class):
        if not items:
            return f"<h2>{title}</h2><p class='status-ok'>✅ None</p>"
        rows = "".join(f"<tr><td>{i}</td></tr>" for i in items)
        return f"<h2>{title}</h2><table><tr><th>File Path</th></tr>{rows}</table>"

    html += list_section("❌ Missing Files", result["missing"], "status-error")
    html += list_section("⚠️ Extra Files", result["extra"], "status-warn")
    html += list_section("🔁 Changed Files", result["changed"], "status-warn")

    if not (result["missing"] or result["extra"] or result["changed"]):
        html += "<h2>✅ Perfect Match!</h2><p>All files match byte-for-byte.</p>"

    html += """
</body></html>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"📄 HTML report saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Compare two project folders and generate HTML report")
    parser.add_argument("original_folder", help="Path to original project folder")
    parser.add_argument("restored_folder", help="Path to restored project folder")
    parser.add_argument("--output", default="compare_report.html", help="Path to output HTML report")
    args = parser.parse_args()

    original_dir = os.path.abspath(args.original_folder)
    restored_dir = os.path.abspath(args.restored_folder)

    print(f"🔍 Comparing:\n  Original: {original_dir}\n  Restored: {restored_dir}")
    result = compare_projects(original_dir, restored_dir)
    generate_html_report(result, args.output)

if __name__ == "__main__":
    main()
