import os
import json
import base64
import zlib
import argparse
from glob import glob

def merge_batches(base_name, input_folder):
    pattern = os.path.join(input_folder, f"{base_name}_part*.txt")
    parts = sorted(glob(pattern))
    if not parts:
        raise FileNotFoundError(f"No parts found for pattern: {pattern}")

    data = b""
    for p in parts:
        with open(p, "rb") as f:
            data += f.read()
        print(f"📦 Merged {os.path.basename(p)}")
    return data

def restore_project(json_text, output_dir):
    data = json.loads(json_text)
    for f in data:
        rel = f["path"]
        path = os.path.join(output_dir, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Always write bytes exactly as stored
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(f["data"]))

        print(f"✅ Restored {rel}")

def main():
    parser = argparse.ArgumentParser(description="Rebuild project from text batches")
    parser.add_argument("base_name", help="Base name of text files (without _partX)")
    parser.add_argument("--input-folder", default="./project_text_output", help="Folder containing text parts")
    args = parser.parse_args()

    input_folder = os.path.abspath(args.input_folder)
    output_folder = os.path.join(input_folder, args.base_name)

    print(f"🔄 Reading parts from: {input_folder}")
    merged = merge_batches(args.base_name, input_folder)

    print("🗜️ Decompressing data...")
    decompressed = zlib.decompress(base64.b64decode(merged))

    print(f"📂 Restoring project into: {output_folder}")
    restore_project(decompressed.decode("utf-8"), output_folder)

    print("🎉 Project successfully restored (exact byte match)!")

if __name__ == "__main__":
    main()
