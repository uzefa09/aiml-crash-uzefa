# Task 9: Mini Inventory System

import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self) -> float:
        return sum(p.price * p.quantity for p in self.products)

    def find_product(self, name: str):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price", "quantity"])
            for p in self.products:
                writer.writerow([p.name, p.price, p.quantity])
        print(f"Saved to {filename}")

    def load_from_csv(self, filename):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_product(Product(row["name"], row["price"], row["quantity"]))

inv = Inventory()
inv.add_product(Product("Laptop", 50000, 10))
inv.add_product(Product("Mouse", 500, 50))
inv.add_product(Product("Keyboard", 1500, 30))

print(f"Total value: {inv.total_value()}")
print(f"Search: {inv.find_product('mouse').name}")
inv.save_to_csv("inventory.csv")