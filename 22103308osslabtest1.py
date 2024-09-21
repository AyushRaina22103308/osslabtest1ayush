import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Welcome To Chemist Shop.")
class ChemistShop:
    def __init__(self):
        self.medicine_names = np.array([])
        self.prices = np.array([], dtype=float)
        self.quantities = np.array([], dtype=int)
        self.total_sales = 0.0
        self.total_profit = 0.0

    def add_item(self, name, price, quantity):
        self.medicine_names = np.append(self.medicine_names, name)
        self.prices = np.append(self.prices, price)
        self.quantities = np.append(self.quantities, quantity)

    def update_quantity(self, name, quantity):
        index = np.where(self.medicine_names == name)[0]
        if index.size > 0:
            self.quantities[index[0]] += quantity
        else:
            print(f"{name} not found in inventory.")

    def sell_item(self, name, quantity):
        index = np.where(self.medicine_names == name)[0]
        if index.size > 0:
            if self.quantities[index[0]] >= quantity:
                self.quantities[index[0]] -= quantity
                sale_amount = quantity * self.prices[index[0]]
                self.total_sales += sale_amount
                self.total_profit += sale_amount * 0.2
                print(f"Sold {quantity} of {name}. Total sale: ${sale_amount:.2f}")
            else:
                print(f"Insufficient stock for {name}.")
        else:
            print(f"{name} not found in inventory.")

    def calculate_total_sales(self):
        print(f"Total sales for the day: ${self.total_sales:.2f}")
        print(f"Total profit for the day: ${self.total_profit:.2f}")

    def display_inventory(self):
        print("Current Inventory:")
        for name, price, quantity in zip(self.medicine_names, self.prices, self.quantities):
            print(f"Name: {name}, Price: ${price:.2f}, Quantity: {quantity}")

if __name__ == "__main__":
    shop = ChemistShop()
    shop.add_item("Aspirin", 5.0, 100)
    shop.add_item("Ibuprofen", 7.5, 50)
    shop.add_item("Paracetamol", 4.0, 200)
    shop.display_inventory()
    shop.update_quantity("Ibuprofen", 30)
    shop.sell_item("Aspirin", 10)
    shop.sell_item("Paracetamol", 20)
    shop.calculate_total_sales()
