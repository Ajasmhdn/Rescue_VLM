import json

path = "/home/cai_tkmce/Desktop/DisasterVLM/raw_data/DisasterM3_Instruct/train_release.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total samples:", len(data))
print("Keys:", list(data[0].keys()))

# print 5 examples of instruction field content
for i in range(3):
    print("\n--- Example", i, "---")
    for k in data[i].keys():
        if "instruction" in k.lower() or "question" in k.lower() or "prompt" in k.lower():
            print(k, ":", data[i][k][:200])
