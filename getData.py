import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("constantinwerner/human-detection-dataset")

# Move to the correct folder
os.rename(path, "./dataset")
path = "./dataset"

print("DONE. Path to dataset files:", path)
