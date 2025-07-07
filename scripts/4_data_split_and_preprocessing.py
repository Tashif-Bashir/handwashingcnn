# Script 4: Data Splitting and Preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image

def preprocess_images(image_paths):
    # Resize and normalize images
    X = []
    for path in image_paths:
        img = Image.open(path).resize((150, 150))
        img = np.array(img) / 255.0  # Normalize to [0,1]
        X.append(img)
    return np.array(X)

# Example usage (assuming valid_data and valid_labels from previous scripts):
# Split into train/val/test (60/20/20 split, stratified)
# X_train, X_temp, y_train, y_temp = train_test_split(valid_data, valid_labels, test_size=0.4, stratify=valid_labels, random_state=42)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)

# X_train = preprocess_images(X_train)
# X_val = preprocess_images(X_val)
# X_test = preprocess_images(X_test)
