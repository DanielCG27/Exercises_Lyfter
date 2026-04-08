import json

def get_pokemon(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        pokemon_type = input("Enter the type that you want to look for: ")

        found_pokemon = [pokemon for pokemon in data if any(t.lower() == pokemon_type.lower() for t in pokemon['type'])]
        
        if not found_pokemon:
            print("That pokemon doesn´t exist.")
        else:
            print("The pokemon of this type are: ")
            for pokemon in found_pokemon:
                print(pokemon['name'])


get_pokemon("Pokemon.json")