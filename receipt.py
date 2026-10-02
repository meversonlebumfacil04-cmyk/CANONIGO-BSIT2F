# receipt.py - presents the official receipt

def print_receipt(orders, menu, subtotal, discount):
    total = subtotal - discount

    print("\n")
    print("==========================================")
    print("            LANCE'S FAST FOOD             ")
    print("             OFFICIAL RECEIPT             ")
    print("==========================================")
    print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>10}{'TOTAL':>12}")
    print("------------------------------------------")

    for item, quantity in orders.items():
        price = menu[item]
        item_total = price * quantity

        print(f"{item:<20}{quantity:>5} "
              f"₱{price:>8.2f} ₱{item_total:>10.2f}")

    print("------------------------------------------")
    print(f"{'Subtotal:':<35} ₱{subtotal:>9.2f}")
    print(f"{'Discount:':<35} ₱{discount:>9.2f}")
    print(f"{'TOTAL:':<35} ₱{total:>9.2f}")
    print("==========================================")
    print("       Thank you for your order!          ")
    print("==========================================")
