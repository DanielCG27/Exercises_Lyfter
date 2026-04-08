sales = [
    {
        "date" : "24/1/2026",
        "costumer_email" : "daniel@gmail.com",
        "item" : [
            {
                "name" : "Helmet",
                "upc" : "H-01",
                "price" : 10
            },
            {
                "name" : "Hammer",
                "upc" : "HR-01",
                "price" : 12
            },
            {
                "name" : "Screw",
                "upc" : "SC-05",
                "price" : 2
            },
        ],
    },
    {
        "date" : "20/1/2026",
        "costumer_email" : "luis@gmail.com",
        "item" : [
            {
                "name" : "Drill",
                "upc" : "DR-08",
                "price" : 80
            },
            {
                "name" : "Screw",
                "upc" : "SC-05",
                "price" : 2
            },
            {
                "name" : "Helmet",
                "upc" : "H-01",
                "price" : 10
            },
        ],
    },
    {
        "date" : "18/1/2026",
        "costumer_email" : "carlos@gmail.com",
        "item" : [
            {
                "name" : "Drill",
                "upc" : "DR-08",
                "price" : 80
            },
            {
                "name" : "Lavatory",
                "upc" : "LV-03",
                "price" : 200
            },
            {
                "name" : "Screw",
                "upc" : "SC-05",
                "price" : 2
            },
        ],
    },
]

result = {}
for sale in sales:
    for item in sale["item"]:
        upc= item["upc"]
        price = item["price"]
        if upc in result:
            result[upc] += price
        else:
            result[upc] = price
print(result)