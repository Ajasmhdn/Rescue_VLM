import json
import os

JSON_PATH = "data/filtered_annotations.json"
IMAGE_DIR = "data/train_images"

with open(JSON_PATH, "r") as f:
    data = json.load(f)

total_samples = len(data)

task_count = {}
image_type_count = {}

for item in data:
    task = item["task"]
    img_type = item.get("post_image_type", "unknown")

    task_count[task] = task_count.get(task, 0) + 1
    image_type_count[img_type] = image_type_count.get(img_type, 0) + 1

print("----- DATASET STATISTICS -----")
print("Total samples:", total_samples)

print("\nTask Distribution:")
for k,v in task_count.items():
    print(f"{k}: {v}")

print("\nImage Type Distribution:")
for k,v in image_type_count.items():
    print(f"{k}: {v}")

# Calculate dataset size
total_size = 0
for file in os.listdir(IMAGE_DIR):
    total_size += os.path.getsize(os.path.join(IMAGE_DIR, file))

print("\nTotal image folder size (GB):", round(total_size / (1024**3), 2))
