import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# -----------------------------
# CONFIG
# -----------------------------
ROOT_PATH = r"E:\AppDumps\Readcomicsonline"
MAX_THREADS = 8
# -----------------------------

def get_folder_info(folder_path: Path):
    total_size = 0
    file_count = 0

    for root, dirs, files in os.walk(folder_path, topdown=True):
        for f in files:
            try:
                fp = os.path.join(root, f)
                total_size += os.path.getsize(fp)
                file_count += 1
            except Exception:
                pass

    return {
        "folder": str(folder_path),
        "size_bytes": total_size,
        "size_mb": round(total_size / (1024 * 1024), 2),
        "size_gb": round(total_size / (1024 * 1024 * 1024), 2),
        "files": file_count
    }


def main():
    root = Path(ROOT_PATH)

    subfolders = [f for f in root.iterdir() if f.is_dir()]

    print(f"Scanning {len(subfolders)} folders using {MAX_THREADS} threads...\n")

    results = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(get_folder_info, folder): folder for folder in subfolders}

        for future in as_completed(futures):
            info = future.result()
            results.append(info)
            print(f"Done: {info['folder']}")

    # sort by size
    results = sorted(results, key=lambda x: x["size_bytes"], reverse=True)

    print("\n=== Folder Sizes ===")
    print(f"{'Folder':60} {'Files':10} {'Size(MB)':10} {'Size(GB)':10}")
    print("-" * 95)

    for r in results:
        print(f"{r['folder'][:58]:60} {r['files']:10} {r['size_mb']:10} {r['size_gb']:10}")


if __name__ == "__main__":
    main()
