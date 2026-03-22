import os
import json
import base64
import zlib
import argparse

MAX_SIZE = 5 * 1024 * 1024  # 5 MB
EXCLUDED_DIRS = {'.git', '.vs', 'bin', 'obj', 'node_modules', '__pycache__', '.idea'}

def collect_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for f in files:
            yield os.path.relpath(os.path.join(root, f), base_dir)

def encode_file_content(path):
    """Read raw bytes and store base64."""
    with open(path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode("ascii")
    return {"encoding": "base64", "data": encoded}

def split_batches(data_bytes, base_output, output_folder):
    total = len(data_bytes)
    os.makedirs(output_folder, exist_ok=True)

    for i, start in enumerate(range(0, total, MAX_SIZE), 1):
        chunk = data_bytes[start:start + MAX_SIZE]
        file_path = os.path.join(output_folder, f"{base_output}_part{i}.txt")
        with open(file_path, "wb") as f:
            f.write(chunk)
        print(f"✅ Created {file_path} ({len(chunk)/1024/1024:.2f} MB)")

def main():
    parser = argparse.ArgumentParser(description="Convert project folder into text batches")
    parser.add_argument("project_folder", help="Path to the project folder")
    parser.add_argument("output_base", help="Base name for output text files")
    parser.add_argument("--output-folder", default="./project_text_output", help="Folder to store text files")
    args = parser.parse_args()

    project_dir = os.path.abspath(args.project_folder)
    output_folder = os.path.abspath(args.output_folder)

    print(f"📁 Scanning project: {project_dir}")
    files = list(collect_files(project_dir))
    print(f"Found {len(files)} files (excluding {', '.join(EXCLUDED_DIRS)})")

    project = []
    for rel in files:
        abs_path = os.path.join(project_dir, rel)
        project.append({"path": rel, **encode_file_content(abs_path)})

    print("🗜️ Compressing project data...")
    json_text = json.dumps(project, separators=(",", ":"))
    compressed = zlib.compress(json_text.encode("utf-8"), level=9)
    encoded = base64.b64encode(compressed)

    print("✂️ Splitting into 5MB parts...")
    split_batches(encoded, args.output_base, output_folder)

    print(f"🎉 Conversion complete! Text files saved in: {output_folder}")

if __name__ == "__main__":
    main()
