import os
import shutil
import math

def batch_images(source_folder, destination_folder, batch_size=100, prefix="Batch"):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of all image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    # Calculate number of subfolders needed
    num_subfolders = math.ceil(len(image_files) / batch_size)

    # Loop to create subfolders
    for i in range(1, num_subfolders + 1):
        subfolder_name = f"{prefix}_{i}"
        subfolder_path = os.path.join(destination_folder, subfolder_name)
        os.makedirs(subfolder_path)

        # Calculate start and end index for image batch
        start_index = (i - 1) * batch_size
        end_index = min(i * batch_size, len(image_files))

        # Loop through image files for this batch
        for index in range(start_index, end_index):
            # Get image file name
            image_file = image_files[index]
            
            # Move image to subfolder
            source_image_path = os.path.join(source_folder, image_file)
            destination_image_path = os.path.join(subfolder_path, image_file)
            shutil.move(source_image_path, destination_image_path)

            print(f"Moved {image_file} to {subfolder_name}")

if __name__ == "__main__":
    source_folder = input("Enter the path to the source folder containing images: ")
    destination_folder = input("Enter the path to the destination folder: ")
    batch_size_input = input("Enter the batch size (default is 100): ")
    prefix = input("Enter the prefix for subfolder names (default is 'Batch'): ")
    
    # Convert batch size to integer if provided, otherwise default to 100
    batch_size = int(batch_size_input) if batch_size_input else 100
    
    # Use default prefix "Batch" if not provided
    prefix = prefix if prefix else "Batch"
    
    batch_images(source_folder, destination_folder, batch_size, prefix)
