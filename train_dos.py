import json

with open("data.json", "r") as f:
    data = json.load(f)

# print(data["examples"][0])

training_data = {
    "classes": ["MEDICINE", "MEDICALCONDITION", "PATHOGEN"],
    "annotations": [],
}
for example in data["examples"]:
    temp_dict = {}
    temp_dict["text"] = example["content"]
    temp_dict["entities"] = []
    for annotation in example["annotations"]:
        start = annotation["start"]
        end = annotation["end"]
        label = annotation["tag_name"].upper()
        temp_dict["entities"].append((start, end, label))
    training_data["annotations"].append(temp_dict)

print(training_data["annotations"][0])
with open("data_train.json", "w") as fp:
    json.dump(training_data, fp)
