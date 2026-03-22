import os

def delete_files_by_extensions(root_dir, extensions, dry_run=False):
    # Normalize extensions: ensure each starts with a dot
    extensions = [ext if ext.startswith(".") else "." + ext for ext in extensions]

    deleted_files = 0

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                file_path = os.path.join(foldername, filename)
                if dry_run:
                    print(f"[Dry-Run] Would delete: {file_path}")
                else:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                        deleted_files += 1
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

    if dry_run:
        print(f"\nDry-run complete. Files matching extensions {extensions} were listed but not deleted.")
    else:
        print(f"\nTotal files deleted with extensions {extensions}: {deleted_files}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Delete files with multiple extensions (with dry-run support).")
    parser.add_argument("directory", help="Root directory to start the search")
    parser.add_argument("extensions", nargs="+", help="File extensions to delete (e.g., .log .tmp .bak)")
    parser.add_argument("--dry-run", action="store_true", help="List files that would be deleted without deleting them")

    args = parser.parse_args()
    delete_files_by_extensions(args.directory, args.extensions, dry_run=args.dry_run)
