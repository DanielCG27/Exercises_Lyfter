class Flyable:

    def fly(self):
        print("The object is flying")


class Swimmable:

    def swim(self):
        print("The object is swimming")

# Herencia múltiple
class Duck(Flyable, Swimmable):

    def quack(self):
        print("Quack quack!")

# Se crea el objeto
duck = Duck()

# Usar métodos heredados
duck.fly()
duck.swim()
duck.quack()