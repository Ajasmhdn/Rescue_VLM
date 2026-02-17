import json
import random
import os
import shutil

random.seed(42)

# -------- PATHS --------
TRAIN_JSON = "data/train.json"
OUTPUT_JSON = "data/mini_train.json"

IMAGE_SOURCE = "data/train_images"
IMAGE_DEST = "data/mini_images"

os.makedirs(IMAGE_DEST, exist_ok=True)

# -------- SETTINGS --------
TOTAL_SAMPLES = 500

# -------- LOAD TRAIN DATA --------
with open(TRAIN_JSON, "r") as f:
    data = json.load(f)

# -------- SEPARATE BY MODALITY --------
optical = [d for d in data if d["post_image_type"] == "Optical"]
sar = [d for d in data if d["post_image_type"] == "SAR"]

total_train = len(data)

opt_ratio = len(optical) / total_train
sar_ratio = len(sar) / total_train

opt_count = int(TOTAL_SAMPLES * opt_ratio)
sar_count = TOTAL_SAMPLES - opt_count

mini_optical = random.sample(optical, opt_count)
mini_sar = random.sample(sar, sar_count)

mini_dataset = mini_optical + mini_sar
random.shuffle(mini_dataset)

# -------- COPY IMAGES --------
copied = 0

for item in mini_dataset:

    # Extract filename safely from Windows-style paths
    pre_filename = item["pre_image_path"].replace("\\", "/").split("/")[-1]
    post_filename = item["post_image_path"].replace("\\", "/").split("/")[-1]

    pre_src = os.path.join(IMAGE_SOURCE, pre_filename)
    post_src = os.path.join(IMAGE_SOURCE, post_filename)

    pre_dst = os.path.join(IMAGE_DEST, pre_filename)
    post_dst = os.path.join(IMAGE_DEST, post_filename)

    if os.path.exists(pre_src):
        shutil.copy2(pre_src, pre_dst)
        copied += 1

    if os.path.exists(post_src):
        shutil.copy2(post_src, post_dst)
        copied += 1

# -------- SAVE MINI JSON (UNCHANGED STRUCTURE) --------
with open(OUTPUT_JSON, "w") as f:
    json.dump(mini_dataset, f, indent=4)

print("Mini dataset created successfully!")
print("Total samples:", len(mini_dataset))
print("Optical:", opt_count)
print("SAR:", sar_count)
print("Images copied:", copied)
