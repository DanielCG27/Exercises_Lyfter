import csv

def get_developer(file_path):
    choose_developer = input("Place the developer that you prefer: ")
    found = False

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        for row in reader:
            developer = row[2]

            if choose_developer == developer:
                name = row[0]
                genre = row[1]
                classification = row[3]
                print(f"{name} (Classification: {classification}, Genre: {genre})")
                found = True
    
    if found == False:
        print("No videogames found for that developer")


get_developer("videogames.csv")