# Script 2: Load Image Paths and Assign Labels
import os
import numpy as np

data_dir = "Data_Repository"
stages = [f"Stage{i}" for i in range(1, 9)]
data = []
labels = []

for stage_index, stage in enumerate(stages):
    stage_path = os.path.join(data_dir, stage)
    for file in os.listdir(stage_path):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            data.append(os.path.join(stage_path, file))
            labels.append(stage_index)

data = np.array(data)
labels = np.array(labels)
