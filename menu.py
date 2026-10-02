# menu.py - displays the menu

def display_menu(menu):
    print("\n========== FAST FOOD MENU ==========")

    for item, price in menu.items():
        print(f"{item:<25} ₱{price:>7.2f}")

    print("====================================")