import json


def save_json(data):

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_json():

    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)