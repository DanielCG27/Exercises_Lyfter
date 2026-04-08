import csv

def get_classification(path_file):
    classification = input("Place the classification: ")
    found = False
    with open(path_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if classification == row[3]:
                print(f"Name: {row[0]}")
                print(f"Genre: {row[1]}")
                print(f"Developer: {row[2]}")
                print(f"Classification: {row[3]}")
                found = True
    if found == False:
        print("No videogames found with that classification")


get_classification("videogames.csv")