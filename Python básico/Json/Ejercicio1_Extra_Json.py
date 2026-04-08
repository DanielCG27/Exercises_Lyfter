import json

def get_information(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            print(f"Name: {i["name"]}, Level: {i["level"]}, Type: {i["type"]}")


get_information("Pokemon.json")