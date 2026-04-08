import json

def get_information(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            if type(i["name"]) == dict:
                name = i["name"] ["english"]

            else:
                name = i["name"]

            if "base" in i:
                attack = i["base"]["Attack"]
                defense = i["base"]["Defense"]
                speed = i["base"]["Speed"]
                print(f"Name: {name}")
                print(f"Attack: {attack}")
                print(f"Defense: {defense}")
                print(f"Speed: {speed}")
            else:
                print(f"Name: {name} (No available)")


get_information("Pokemon.json")