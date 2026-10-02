# pricing.py - calculates subtotal and discount

def calculate_total(orders, menu):
    subtotal = 0

    for item, quantity in orders.items():
        subtotal += menu[item] * quantity

    return subtotal


def calculate_discount(subtotal):
    # 10% discount for orders worth ₱1,000 or more
    if subtotal >= 1000:
        return subtotal * 0.10
    else:
        return 0