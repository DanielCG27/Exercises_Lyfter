list_1 = ["Name", "Country", "City", "Age"]
list_2 = ["Daniel", "Costa Rica", "San Jose", 31]
dict = {}
for information in range(len(list_1)):
    dict[list_1[information]] = list_2[information]
print(dict) 