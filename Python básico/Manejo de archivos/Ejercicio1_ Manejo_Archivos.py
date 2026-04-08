# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los 
# mismos nombres ordenados alfabéticamente.

def sort_songs(file_path, output_path):
    with open(file_path, "r", encoding="utf-8") as file:
        songs = file.readlines()

    songs.sort()

    for song in songs:
        print(song.strip())

    with open(output_path, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song)  


sort_songs("Songs.txt", "sorted_songs.txt")