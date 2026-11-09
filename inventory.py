# Inventory + Sales Management System

inventory = {}
sales = []


# 1. Add Item
def add_item():
    item_id = input("Enter Item ID: ")

    if item_id in inventory:
        print("Item already exists!")
        return

    name = input("Enter Item Name: ")
    stock = int(input("Enter Stock: "))
    price = float(input("Enter Price: "))

    if stock < 0 or price < 0:
        print("Stock and price cannot be negative!")
        return

    inventory[item_id] = {
        "Name": name,
        "Stock": stock,
        "Price": price
    }

    print("Item added successfully!")


# 2. Show Items
def show_items():
    if not inventory:
        print("Inventory is empty!")
        return

    for item_id, item in inventory.items():
        print(
            "ID:", item_id,
            "| Name:", item["Name"],
            "| Stock:", item["Stock"],
            "| Price:", item["Price"]
        )


# 3. Sell Item
def sell_item():
    item_id = input("Enter Item ID: ")

    if item_id not in inventory:
        print(f"Item ID {item_id} not found!")
        return

    quantity = int(input("Enter Quantity: "))

    if quantity <= 0:
        print("Quantity must be positive!")
        return

    item = inventory[item_id]

    if quantity > item["Stock"]:
        print("Not enough stock!")
        print("Available stock:", item["Stock"])
        return

    revenue = quantity * item["Price"]
    item["Stock"] -= quantity

    sales.append({
        "ID": item_id,
        "Name": item["Name"],
        "Quantity": quantity,
        "Amount": revenue
    })

    print("Sale recorded!")
    print("Revenue:", revenue)
    print("Stock left:", item["Stock"])


# 4. Update Item
def update_item():
    item_id = input("Enter Item ID: ")

    if item_id not in inventory:
        print("Item not found!")
        return

    item = inventory[item_id]

    name = input("Enter New Name: ")
    stock = int(input("Enter New Stock: "))
    price = float(input("Enter New Price: "))

    if not name or stock < 0 or price < 0:
        print("Invalid details!")
        return

    item["Name"] = name
    item["Stock"] = stock
    item["Price"] = price

    print("Item updated successfully!")


# 5. Delete Item
def delete_item():
    item_id = input("Enter Item ID: ")

    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully!")
    else:
        print("Item not found!")


# 6. Sales Report
def sales_report():
    if not sales:
        print("No sales recorded!")
        return

    total_revenue = 0
    sold_units = {}

    for sale in sales:
        total_revenue += sale["Amount"]

        name = sale["Name"]
        sold_units[name] = (
            sold_units.get(name, 0) + sale["Quantity"]
        )

    print("\n--- Sales Report ---")

    for name, quantity in sold_units.items():
        print(name, ":", quantity, "units")

    print("Total Revenue:", total_revenue)

    best_seller = max(sold_units, key=sold_units.get)
    print("Best Seller:", best_seller)


# Main Menu
def main():
    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Add Item")
        print("2. Sell Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Sales Report")
        print("6. Show Items")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            sell_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            sales_report()
        elif choice == "6":
            show_items()
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()