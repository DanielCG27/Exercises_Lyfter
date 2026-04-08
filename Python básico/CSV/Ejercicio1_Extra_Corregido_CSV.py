import csv

def get_file(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            print(f"Name: {row[0]}")
            print(f"Genre: {row[1]}")
            print(f"Developer: {row[2]}")
            print(f"Classification: {row[3]}")

get_file("videogames.csv")