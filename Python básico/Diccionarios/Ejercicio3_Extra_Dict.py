sales= [
    {"name": "Computer", "category" : "Electronic", "price" : 500},
    {"name" : "Mouse", "category" : "Electronic", "price" : 5},
    {"name" : "Gypsum", "category" : "construction", "price" : 10},
    {"name" : "Drill", "category" : "construction", "price" : 100}
]

result= {}
for sale in sales:
    category= sale["category"]
    price= sale["price"]

    if category not in result:
        result[category] = 0
    result[category] += price
print(result)