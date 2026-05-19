class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.persons = []
        

    def add_passenger(self, person):
        if len(self.persons) < self.max_passengers:
            self.persons.append(person)
            print(f"{person.name} added successfully")
        else:
            print("The bus is full. Cannot add more passengers")


    def remove_passenger(self, person):
        if person in self.persons:
            self.persons.remove(person)
            print(f"{person.name} has been removed from the bus")
        else:
            (f"{person.name} is not on the bus")


class person:
    def __init__(self, name):
        self.name = name


bus = Bus(3)
person1 = person("Daniel")
person2 = person("Sofía")
person3 = person("Jose")


bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)