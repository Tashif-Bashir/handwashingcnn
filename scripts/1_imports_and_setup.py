# Script 1: Import Required Libraries and Setup
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import pathlib
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight

# Optional: Delete corrupted MobileNetV2 weights if present
def delete_corrupted_weights():
    keras_models_dir = pathlib.Path.home() / ".keras" / "models"
    corrupted_file = keras_models_dir / "mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5"
    if corrupted_file.exists():
        print(f"Deleting corrupted weights file: {corrupted_file}")
        corrupted_file.unlink()
    else:
        print("No corrupted weights file found.")

# Execute deletion check
delete_corrupted_weights()
