import os
from shutil import SameFileError, copy2

import kagglehub

# Download latest version
path = kagglehub.dataset_download(
    "shashwatwork/dataco-smart-supply-chain-for-big-data-analysis"
)
print("Path to dataset files:", path)


files = os.listdir(path)

for file in files:
    print(file)

source_file = f"{path}/DataCoSupplyChainDataset.csv"
destination_file = "../data/raw/"

os.makedirs(destination_file, exist_ok=True)

try:
    # Use shutil.copy2 to copy file and metadata
    copy2(source_file, destination_file)
    print(f"File copied successfully to {destination_file}")
except SameFileError:
    print("Source and destination represent the same file.")
except PermissionError:
    print("Permission denied.")
except IsADirectoryError:
    print(
        "Destination is a directory (use shutil.copy() instead of copyfile/copy2 if this is the intent)."
    )
except FileNotFoundError as e:
    print(f"File or directory not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
