# Script 3: Label Validation and Error Checking
from PIL import Image
import numpy as np

def check_label_errors(data, labels, stages):
    valid_data = []
    valid_labels = []
    invalid_size_data = []
    invalid_size_labels = []
    error_count = 0
    invalid_format_count = 0
    incorrect_folder_count = 0

    for i, path in enumerate(data):
        if not path.lower().endswith(('.jpg', '.jpeg', '.png')):
            invalid_format_count += 1
            print(f"Invalid format: {path}")
            continue

        try:
            img = Image.open(path)
            img.verify()  # Check image integrity
            img = Image.open(path)  # Re-open to check size
            if img.size != (150, 150):
                invalid_size_data.append(path)
                invalid_size_labels.append(labels[i])
                print(f"Invalid size: {path} with size {img.size}")
                continue

            expected_stage = stages[labels[i]]
            if expected_stage not in path:
                incorrect_folder_count += 1
                print(f"Incorrect folder: {path} expected in {expected_stage}")
                continue

            valid_data.append(path)
            valid_labels.append(labels[i])

        except Exception as e:
            error_count += 1
            print(f"Error opening image {path}: {e}")

    print(f"Total images with invalid formats: {invalid_format_count}")
    print(f"Total images in incorrect folders: {incorrect_folder_count}")
    print(f"Total images that cannot be opened: {error_count}")
    print(f"Total images with invalid sizes: {len(invalid_size_data)}")

    return (np.array(valid_data), np.array(valid_labels),
            np.array(invalid_size_data), np.array(invalid_size_labels))
