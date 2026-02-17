import json
import random

INPUT_JSON = "data/filtered_annotations.json"

TRAIN_JSON = "data/train.json"
VAL_JSON = "data/val.json"
TEST_JSON = "data/test.json"

with open(INPUT_JSON, "r") as f:
    data = json.load(f)

optical = [d for d in data if d.get("post_image_type") == "Optical"]
sar = [d for d in data if d.get("post_image_type") == "SAR"]

def split_group(group):
    random.shuffle(group)
    n = len(group)
    train_end = int(0.8 * n)
    val_end = int(0.9 * n)
    return group[:train_end], group[train_end:val_end], group[val_end:]

opt_train, opt_val, opt_test = split_group(optical)
sar_train, sar_val, sar_test = split_group(sar)

train_data = opt_train + sar_train
val_data = opt_val + sar_val
test_data = opt_test + sar_test

random.shuffle(train_data)
random.shuffle(val_data)
random.shuffle(test_data)

with open(TRAIN_JSON, "w") as f:
    json.dump(train_data, f, indent=4)

with open(VAL_JSON, "w") as f:
    json.dump(val_data, f, indent=4)

with open(TEST_JSON, "w") as f:
    json.dump(test_data, f, indent=4)

print("Stratified split completed!")
print("Train:", len(train_data))
print("Val:", len(val_data))
print("Test:", len(test_data))
