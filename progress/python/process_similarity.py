import os
import json
import shutil

def load_similarity_data(json_file):
    """Load similarity data from the JSON file."""
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"The file '{json_file}' does not exist.")
    with open(json_file, "r") as f:
        data = json.load(f)
    return data

def find_high_similarity_pairs(data, threshold=90):
    """
    Find pairs of images with similarity above a threshold.
    
    Args:
        data (dict): The JSON data containing similarity scores.
        threshold (int): The similarity percentage threshold.

    Returns:
        list: A list of tuples (image1, image2, similarity).
    """
    high_similarity_pairs = []
    for item in data:
        if item["similarity"] >= threshold:
            high_similarity_pairs.append((item["image1"], item["image2"], item["similarity"]))
    return high_similarity_pairs

def move_files(file_pairs, target_folder):
    """Move one of the files in each pair to a target folder."""
    os.makedirs(target_folder, exist_ok=True)
    for file1, file2, similarity in file_pairs:
        # Move the first file as an example (you can modify the logic as needed)
        if os.path.exists(file1):
            target_path = os.path.join(target_folder, os.path.basename(file1))
            shutil.move(file1, target_path)
            print(f"Moved {file1} to {target_folder}")

def delete_smaller_files(file_pairs):
    """Delete the file with the smaller size in each pair."""
    for file1, file2, similarity in file_pairs:
        if os.path.exists(file1) and os.path.exists(file2):
            size1 = os.path.getsize(file1)
            size2 = os.path.getsize(file2)
            if size1 < size2:
                os.remove(file1)
                print(f"Deleted smaller file: {file1}")
            else:
                os.remove(file2)
                print(f"Deleted smaller file: {file2}")

def process_options(file_pairs, option, target_folder=None):
    """
    Process similar files based on the selected option.

    Args:
        file_pairs (list): List of file pairs with high similarity.
        option (str): 'move' to move files, 'delete' to delete smaller files.
        target_folder (str): Target folder for moving files (required for 'move').
    """
    if option == "move":
        if target_folder is None:
            raise ValueError("Target folder must be specified for 'move' option.")
        move_files(file_pairs, target_folder)
    elif option == "delete":
        delete_smaller_files(file_pairs)
    else:
        raise ValueError("Invalid option. Choose 'move' or 'delete'.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process JSON file with similarity data.")
    parser.add_argument("json_file", help="Path to the JSON file containing similarity data.")
    parser.add_argument("--threshold", type=int, default=90, help="Similarity threshold (default: 90).")
    parser.add_argument("--option", choices=["move", "delete"], required=True, help="Action to perform: move or delete.")
    parser.add_argument("--target_folder", help="Target folder for moving files (required for 'move').")

    args = parser.parse_args()

    try:
        # Load the similarity data
        similarity_data = load_similarity_data(args.json_file)

        # Find pairs with high similarity
        similar_pairs = find_high_similarity_pairs(similarity_data, args.threshold)
        if not similar_pairs:
            print("No similar files found above the specified threshold.")
        else:
            print(f"Found {len(similar_pairs)} similar file pairs with similarity >= {args.threshold}%.")
            for pair in similar_pairs:
                print(f"Similar: {pair[0]} <--> {pair[1]} ({pair[2]}%)")

            # Process the pairs based on the selected option
            process_options(similar_pairs, args.option, args.target_folder)

    except Exception as e:
        print(f"Error: {e}")
