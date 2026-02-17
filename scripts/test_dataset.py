from datasets import load_dataset

print("Loading dataset from HuggingFace...")
ds = load_dataset("Kingdrone-Junjue/DisasterM3")

print("\nDataset loaded successfully ✅")
print("Available splits:", ds.keys())

split = list(ds.keys())[0]
print("Using split:", split)

item = ds[split][0]
print("\nKeys in one sample:", list(item.keys()))

print("\nPreview one sample:")
for k, v in item.items():
    print(f"{k}: {type(v)}")
