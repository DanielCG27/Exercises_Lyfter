import csv

def video_games(file_path):
    quantity = int(input("How many videogames do you want to add? "))
    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")

    
        writer.writerow(["Name", "Genre","Developer", "Classification"])

        for i in range(quantity):
            name = input("Place the videogame name: ")
            genre = input("Place the videogame genre: ")
            developer = input("Place the videogame developer: ")
            classification = input("Place the videogame classification: ")        
            writer.writerow([name, genre, developer, classification])


video_games("videogames.tsv")