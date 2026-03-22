import os
import subprocess
import sys

#pip install torch torchvision scikit-learn numpy pillow argparse logging

# Required modules
required_modules = [
    "torch", "torchvision", "numpy", "scikit-learn", "pillow", "argparse", "logging"
]


# Import installed modules
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import numpy as np
import json
import pickle
from PIL import Image
import argparse
import logging
from multiprocessing import Pool

# Global variables for model, transform, and device
model = None
transform = None
device = None

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
def numpy_converter(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()  # Convert NumPy arrays to lists
    elif isinstance(obj, np.float32):  # Handle np.float32 and other NumPy scalars
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")
        
def validate_folder_path(path):
    """Validate and sanitize the folder path."""
    if not os.path.exists(path):
        raise ValueError(f"Folder does not exist: {path}")
    if not os.path.isdir(path):
        raise ValueError(f"Provided path is not a folder: {path}")
    return os.path.abspath(path)

def safe_save(data, file_path):
    """Save data safely, ensuring backups."""
    temp_file = file_path + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(data, f, default=numpy_converter, indent=4)
    os.replace(temp_file, file_path)

def extract_features(image_path, model, transform, device):
    """Extract features from an image using a pre-trained model."""
    try:
        image = Image.open(image_path).convert("RGB")
        image = transform(image).unsqueeze(0).to(device)
        with torch.no_grad():
            features = model(image).cpu().numpy().flatten()
        return features
    except FileNotFoundError:
        logger.error(f"File not found: {image_path}")
    except OSError as e:
        logger.error(f"OS error processing {image_path}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error processing {image_path}: {e}", exc_info=True)
    return None

def initialize_model():
    """Initialize the ResNet50 model and transformations."""
    global model, transform, device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = resnet50(pretrained=True).to(device)
    model = torch.nn.Sequential(*(list(model.children())[:-1]))  # Remove the final layer
    model.eval()

    # Define image transformations
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

def process_image_path(image_path):
    """Process a single image to extract features."""
    from PIL import Image
    try:
        global model, transform, device
        img = Image.open(image_path).convert("RGB")
        img_tensor = transform(img).unsqueeze(0).to(device)  # Add batch dimension
        with torch.no_grad():
            features = model(img_tensor).cpu().numpy().flatten()
        return image_path, features
    except Exception as e:
        logger.error(f"Error processing image {image_path}: {e}")
        return image_path, None

def compare_images(features, image_paths, result_file):
    """Compare images based on features and store similarity results."""
    logger.info("Comparing images...")
    
    # Calculate pairwise similarities
    similarity_matrix = cosine_similarity(features)
    results = []
    for i in range(len(features)):
        for j in range(i + 1, len(features)):
            similarity = similarity_matrix[i, j]
            result = {
                "image_1": image_paths[i],
                "image_2": image_paths[j],
                "similarity": similarity
            }
            results.append(result)

    # Save results
    logger.info(f"Saving comparison results to {result_file}...")
    safe_save(results, result_file)
    logger.info(f"Saved {len(results)} comparisons to {result_file}")

def process_images(folder_path, output_filename="image_features.pkl", result_file="image_comparison.json", cluster_count=10):
    """Process images, including new images, extract features, perform clustering, and compare."""
    folder_path = validate_folder_path(folder_path)
    output_file = os.path.join(folder_path, output_filename)
    result_file = os.path.join(folder_path, result_file)

    # Initialize variables
    features = []
    valid_paths = []
    processed_paths = set()  # Keep track of previously processed paths

    # Check if the features file already exists
    if os.path.exists(output_file):
        logger.info(f"Features file found: {output_file}. Loading saved features...")
        with open(output_file, "rb") as f:
            data = pickle.load(f)
            features = data["features"]
            valid_paths = data["paths"]
            processed_paths = set(valid_paths)  # Convert to set for fast lookup

    # Identify new images to process
    image_paths = [os.path.join(folder_path, fname) for fname in os.listdir(folder_path)
                   if fname.lower().endswith(('.png', '.jpg', '.jpeg'))]
    new_image_paths = [path for path in image_paths if path not in processed_paths]

    if not new_image_paths:
        logger.info("No new images to process. Using existing features.")
    else:
        logger.info(f"Found {len(new_image_paths)} new images to process.")

        # Initialize model in the main process
        initialize_model()

        # Process new images using multiprocessing
        with Pool(processes=os.cpu_count(), initializer=initialize_model) as pool:
            results = pool.map(process_image_path, new_image_paths)

        # Collect results for new images
        new_features = []
        for path, feature in results:
            if feature is not None:
                new_features.append(feature)
                valid_paths.append(path)

        if not new_features:
            logger.warning("No valid features extracted from new images.")
        else:
            # Merge new features with existing ones
            if features is not None and features.size > 0:
                features = np.vstack([features, np.array(new_features)])
            else:
                features = np.array(new_features)

            # Save updated features
            with open(output_file, "wb") as f:
                pickle.dump({"features": features, "labels": [], "paths": valid_paths}, f)
            logger.info(f"Updated features saved to {output_file}")

        # Save updated features
        with open(output_file, "wb") as f:
            pickle.dump({"features": features, "labels": [], "paths": valid_paths}, f)
        logger.info(f"Updated features saved to {output_file}")

    # Dimensionality reduction
    pca = PCA(n_components=min(len(features), features.shape[1], 50))
    reduced_features = pca.fit_transform(features)

    # Perform clustering
    logger.info(f"Clustering features into {cluster_count} clusters...")
    kmeans = KMeans(n_clusters=cluster_count, random_state=42).fit(reduced_features)
    logger.info(f"Clustering completed. Labels assigned.")

    # Compare images and store results
    compare_images(features, valid_paths, result_file)

def load_features(file_path):
    """Load precomputed features from a file."""
    with open(file_path, "rb") as f:
        data = pickle.load(f)
    return data["features"], data.get("labels", []), data["paths"]

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Image Comparison with Feature Extraction")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing images")
    parser.add_argument("--output_filename", type=str, default="image_features.pkl", help="Filename to save extracted features in the same folder")
    parser.add_argument("--result_file", type=str, default="image_comparison.json", help="Filename to save image comparison results")
    parser.add_argument("--clusters", type=int, default=10, help="Number of clusters for K-Means")
    args = parser.parse_args()

    # Process images with given arguments
    process_images(args.folder_path, args.output_filename, args.result_file, args.clusters)
