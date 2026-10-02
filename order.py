# order.py - asks for the customer's order

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity
            else:
                print("Please enter a quantity greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_order(menu):
    orders = {}

    while True:
        item = input("\nEnter menu item: ").strip().title()

        if item in menu:
            quantity = get_quantity()

            if item in orders:
                orders[item] += quantity
            else:
                orders[item] = quantity

            print(f"{quantity} x {item} added to your order.")

            another = input("Do you want to order another item? (yes/no): ").lower()

            if another == "no":
                break
            elif another != "yes":
                print("Invalid choice. Returning to your order.")
                break

        else:
            print("Sorry, that item is not on the menu.")
            print("Please choose an item from the menu.")

    return orders