import json
import os
import shutil

# -------- PATHS --------
INPUT_JSON = "/home/cai_tkmce/Desktop/DisasterVLM/raw_data/DisasterM3_Instruct/train_release.json"
INPUT_IMG_ROOT = "/home/cai_tkmce/Desktop/DisasterVLM/raw_data/DisasterM3_Instruct"

OUTPUT_JSON = "/home/cai_tkmce/Desktop/DisasterVLM/data/filtered_annotations.json"
OUTPUT_IMG_DIR = "/home/cai_tkmce/Desktop/DisasterVLM/data/train_images"

TARGET_TASKS = [
    "disaster caption",
    "disaster restoration advice"
]

os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

filtered = []
copied = 0

for item in data:
    if item.get("task") in TARGET_TASKS:

        filtered.append(item)

        # JSON already contains relative path
        pre_rel = item["pre_image_path"].replace("\\", "/")
        post_rel = item["post_image_path"].replace("\\", "/")

        pre_src = os.path.join(INPUT_IMG_ROOT, pre_rel)
        post_src = os.path.join(INPUT_IMG_ROOT, post_rel)

        pre_dst = os.path.join(OUTPUT_IMG_DIR, os.path.basename(pre_rel))
        post_dst = os.path.join(OUTPUT_IMG_DIR, os.path.basename(post_rel))

        if os.path.exists(pre_src):
            shutil.copy(pre_src, pre_dst)
            copied += 1
        else:
            print("Missing:", pre_src)

        if os.path.exists(post_src):
            shutil.copy(post_src, post_dst)
            copied += 1
        else:
            print("Missing:", post_src)

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(filtered, f, indent=4)

print("Filtering completed!")
print("Samples kept:", len(filtered))
print("Images copied:", copied)
