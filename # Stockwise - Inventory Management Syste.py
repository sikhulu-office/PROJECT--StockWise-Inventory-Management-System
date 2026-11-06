# Stockwise - Inventory Management System

# Task 1: create two or more product dictionaries. Choose your own product names, prices and quantities.
# Task 2: Put all three products into a list. Name the list: inventory
# Task 3: Use a for loop to display each product's name, price, quantity and total stock value.
# Task 4: Calculate the total inventory value.
# Task 5: Identify products with fewer than 10 units remaining.
# Task 6: Count how many products need restocking and how many units are in those products' stock.
# Task 7: Create a product search feature.
# Task 8: Product search.
# Task 9: Allow user to restock or add a new product.
# Task 10: Update the inventory.
# Task 11: Input validation (using try and except).
# Task 12: Create a menu.

import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(BASE_DIR, "inventory.json")


product_1 = {
    "name": "Notebook",
    "price": 25.00,
    "quantity": 10
}

product_2 = {
    "name": "Pen",
    "price": 5.00,
    "quantity": 20
}

product_3 = {
    "name": "Eraser",
    "price": 6.00,
    "quantity": 15
}

product_4 = {
    "name": "Pencil",
    "price": 5.00,
    "quantity": 7
}

product_5 = {
    "name": "Ruler",
    "price": 10.00,
    "quantity": 10
}

product_6 = {
    "name": "Sharpener",
    "price": 8.00,
    "quantity": 17
}

product_7 = {
    "name": "Stapler",
    "price": 30.00,
    "quantity": 11
}


inventory = [product_1, product_2, product_3, product_4, product_5, product_6, product_7]


def save_inventory():
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def load_inventory():
    global inventory

    try:
        with open(INVENTORY_FILE, "r") as file:
            saved_inventory = json.load(file)

            if saved_inventory:
                inventory = saved_inventory
            else:
                save_inventory()
                
    except (FileNotFoundError, json.JSONDecodeError):
        save_inventory()


def view_inventory():
    total_inventory_value = 0
    
    print("\n===== STOCKWISE INVENTORY =====")
    
    for product in inventory:
        name = product["name"]
        price = product["price"]
        quantity = product["quantity"]
        
        stock_value = price * quantity
        total_inventory_value += stock_value
        
        print(f"Product: {name}")
        print(f"Price: R{price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Stock value: R{stock_value:.2f}")
        print()
    
    print(f"Total inventory value: R{total_inventory_value:.2f}")


def view_low_stock():
    print("\n===== LOW STOCK =====")

    low_stock_found = False

    for product in inventory:
        if product["quantity"] < 10:
            print(f"LOW STOCK: {product['name']} - Only {product['quantity']} left!")
            low_stock_found = True

    if not low_stock_found:
        print("No products are currently low on stock.")


def view_restocking_summary():
    low_stock_count = 0
    low_stock_units = 0

    print("\n===== RESTOCKING SUMMARY ====")

    for product in inventory:
        if product["quantity"] < 10:
            low_stock_count += 1
            low_stock_units += product["quantity"]

    print(f"Products needing restock: {low_stock_count}")
    print(f"Units remaining in low-stock products: {low_stock_units}")


def search_product():
    print("\n===== PRODUCT SEARCH =====")

    search_name = input("Enter the product name to search: ")

    found = False

    for product in inventory:
        if product["name"].lower() == search_name.lower():
            print("Product found!")
            print(f"Name: {product['name']}")
            print(f"Price: R{product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")

            found = True
            break

    if not found:
        print("Product not found.")


def restock_product():
    print("\n===== RESTOCK EXISTING PRODUCT =====")

    restock_name = input("Enter the product name to restock: ")

    product_found = False

    for product in inventory:
        if product["name"].lower() == restock_name.lower():
            print(f"Product found: {product['name']}")
            print(f"Current quantity: {product['quantity']}")

            while True:
                try:
                    additional_stock = int(input("Enter the additional stock: "))

                    if additional_stock <= 0:
                        print("Additional stock must be greater than zero. Try again.")
                        continue

                    break

                except ValueError:
                    print("Invalid quantity! Please enter a whole number.")

            product["quantity"] += additional_stock
            save_inventory()

            print("Stock updated successfully!")
            print(f"New quantity: {product['quantity']}")

            product_found = True
            break

    if not product_found:
        print("Product not found in inventory.")


def add_product():
    print("\n===== ADD NEW PRODUCT =====")
    new_name = input("Enter the new product name (or type 'CANCEL' to abort): ")

    if new_name == "CANCEL":
        print("Product addition cancelled.")
        return

    product_exists = False

    for product in inventory:
        if product["name"].lower() == new_name.lower():
            product_exists = True
            break

    if product_exists:
        print("This product already exists in the inventory.")
        print("Use the restock option to increase its quantity.")
        return

    while True:
        price_input = input("Enter the product price (or type 'CANCEL' to abort): ")

        if price_input == "CANCEL":
            print("Product addition cancelled.")
            return

        try:
            new_price = float(price_input)
            if new_price < 0:
                print("Price cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid price! Please enter a number.")

    while True:
        quantity_input = input("Enter the quantity (or type 'CANCEL' to abort): ")

        if quantity_input == "CANCEL":
            print("Product addition cancelled.")
            return

        try:
            new_quantity = int(quantity_input)
            if new_quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity! Please enter a whole number.")

    new_product = {
        "name": new_name,
        "price": new_price,
        "quantity": new_quantity
    }

    inventory.append(new_product)
    save_inventory()

    print("\nProduct added successfully!")
    print(f"Product name: {new_product['name']}")
    print(f"Price: R{new_product['price']:.2f}")
    print(f"Quantity: {new_product['quantity']}")


def main_menu():
    while True:
        print("\n===== STOCKWISE MAIN MENU =====")
        print("1. View inventory")
        print("2. Search product")
        print("3. Add product")
        print("4. Restock existing product")
        print("5. View low-stock alerts")
        print("6. View restocking summary")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            search_product()

        elif choice == "3":
            add_product()

        elif choice == "4":
            restock_product()

        elif choice == "5":
            view_low_stock()

        elif choice == "6":
            view_restocking_summary()

        elif choice == "7":
            print("Thank you for using StockWise!")
            break
        
        else:
            print("Invalid option. Please try again.")


load_inventory()

main_menu()

