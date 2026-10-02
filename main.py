# main.py - executes all functions
from menu import display_menu
from order import get_order
from pricing import calculate_total, calculate_discount
from receipt import print_receipt


def main():
    menu = {
        "Burger": 120,
        "Cheeseburger": 150,
        "Chicken": 180,
        "French Fries": 80,
        "Spaghetti": 130,
        "Fried Chicken": 160,
        "Soft Drink": 50,
        "Iced Tea": 60
    }

    display_menu(menu)

    while True:
        choice = input("\nDo you want to order? (yes/no): ").lower()

        if choice == "yes":
            break
        elif choice == "no":
            print("\nThank you! Have a nice day!")
            return
        else:
            print("Invalid input! Please enter yes or no.")

    orders = get_order(menu)

    if len(orders) == 0:
        print("\nNo items were ordered.")
        print("Thank you for visiting!")
        return

    subtotal = calculate_total(orders, menu)
    discount = calculate_discount(subtotal)

    print_receipt(orders, menu, subtotal, discount)


main()