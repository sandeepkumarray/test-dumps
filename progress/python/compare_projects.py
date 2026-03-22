import os
import hashlib
import argparse

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
    restored_files = collect_files(restored_dir)

    orig_set = set(orig_files.keys())
    restored_set = set(restored_files.keys())

    missing_in_restored = sorted(orig_set - restored_set)
    extra_in_restored = sorted(restored_set - orig_set)
    common_files = sorted(orig_set & restored_set)

    changed_files = []
    for rel in common_files:
        if hash_file(orig_files[rel]) != hash_file(restored_files[rel]):
            changed_files.append(rel)

    print("\n🧩 Comparison Summary")
    print("-" * 60)
    print(f"Total Original Files : {len(orig_files)}")
    print(f"Total Restored Files : {len(restored_files)}")
    print(f"Missing in Restored  : {len(missing_in_restored)}")
    print(f"Extra in Restored    : {len(extra_in_restored)}")
    print(f"Changed Files        : {len(changed_files)}")
    print("-" * 60)

    if missing_in_restored:
        print("\n❌ Missing files in restored project:")
        for f in missing_in_restored:
            print("   ", f)

    if extra_in_restored:
        print("\n⚠️ Extra files found in restored project:")
        for f in extra_in_restored:
            print("   ", f)

    if changed_files:
        print("\n🔁 Files with modified content:")
        for f in changed_files:
            print("   ", f)

    if not (missing_in_restored or extra_in_restored or changed_files):
        print("\n✅ All files match perfectly!")

def main():
    parser = argparse.ArgumentParser(description="Compare two project folders for discrepancies")
    parser.add_argument("original_folder", help="Path to original project folder")
    parser.add_argument("restored_folder", help="Path to restored project folder")
    args = parser.parse_args()

    original_dir = os.path.abspath(args.original_folder)
    restored_dir = os.path.abspath(args.restored_folder)

    if not os.path.isdir(original_dir):
        print(f"❌ Original folder not found: {original_dir}")
        return
    if not os.path.isdir(restored_dir):
        print(f"❌ Restored folder not found: {restored_dir}")
        return

    print(f"🔍 Comparing:\n  Original: {original_dir}\n  Restored: {restored_dir}")
    compare_projects(original_dir, restored_dir)

if __name__ == "__main__":
    main()
