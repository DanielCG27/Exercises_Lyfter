import csv

def get_file(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        for i in reader:
            print(i)


get_file("videogames.csv")