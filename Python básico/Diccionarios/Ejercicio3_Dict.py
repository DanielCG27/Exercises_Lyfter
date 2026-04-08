list= ["Country", "Age"]
dict = {
    "name" : "Daniel",
    "last_name" : "Camacho",
    "Country" : "Costa Rica",
    "Age" : 31
}

for key in list:
    if key in dict:
        del dict[key]
print(dict)