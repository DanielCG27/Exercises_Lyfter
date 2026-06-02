class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity



class Inventory:
    def __init__(self):
        self.products = []


    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added successfully")


    def show_product(self):
        print("Products in inventory")
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")


    def calculate_inventory(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value


product1 = Product("Pencil", 10, 5)
product2 = Product("Eraser", 5, 25)
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.show_product()
total_value = inventory.calculate_inventory()
print(f"Total inventory value: {total_value}")