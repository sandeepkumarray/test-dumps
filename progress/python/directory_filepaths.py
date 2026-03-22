import os
import csv
import sys
from datetime import datetime

def generate_directory_report(root_dir, output_csv_path=None):
    # Create timestamped filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    default_filename = f"directory_report_{timestamp}.csv"

    # Determine output path
    if output_csv_path:
        # If just a base name, save in current working dir or as specified
        if not output_csv_path.lower().endswith('.csv'):
            output_csv_path += f"_{timestamp}.csv"
        else:
            base, ext = os.path.splitext(output_csv_path)
            output_csv_path = f"{base}_{timestamp}{ext}"
    else:
        output_csv_path = os.path.join(root_dir, default_filename)

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['File Paths'])

        for dirpath, dirnames, filenames in os.walk(root_dir):
            subdir_count = len(dirnames)
            file_count = len(filenames)
            for filename in filenames:
                writer.writerow([dirpath + '\\' + filename])

    print(f"Report generated: {output_csv_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python directory_report.py <root_directory> [output_csv_base_name]")
        sys.exit(1)

    root_directory = sys.argv[1]
    output_csv_base = sys.argv[2] if len(sys.argv) >= 3 else None

    if not os.path.isdir(root_directory):
        print(f"Error: '{root_directory}' is not a valid directory.")
        sys.exit(1)

    generate_directory_report(root_directory, output_csv_base)
