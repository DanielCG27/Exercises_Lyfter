employees= [
    {
        "name" : "Carlos Vargas",
        "email" : "carlos@gmail.com",
        "department" : "HR"
    },
    {
        "name" : "Daniel Camacho",
        "email" : "daniel@gmail.com",
        "department" : "IT"
    },
    {
        "name" : "Sofía Valverde",
        "email" : "sofia@gmail.com",
        "department" : "IT" 
    },
    {
        "name" : "Luis Gómez",
        "email" : "luis@gmail.com",
        "department" : "HR"
    }
]
grouped = {}

for employee in employees:
    department = employee["department"]
    if department not in grouped:
        grouped[department] = []
    grouped[department].append(employee)
print(grouped)