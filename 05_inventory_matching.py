"""
Problem:
Check if order can be fulfilled within budget. Prioritize lower prices.
"""

def can_fulfill_order(inventory, order_quantity, budget):
    sorted_inventory = sorted(inventory.items(), key=lambda x: x[1]['price'])
    total_cost = 0
    fulfilled = 0

    for product, info in sorted_inventory:
        qty = min(info['quantity'], order_quantity - fulfilled)
        cost = qty * info['price']
        if total_cost + cost > budget:
            continue
        fulfilled += qty
        total_cost += cost
        if fulfilled == order_quantity:
            break

    if fulfilled == order_quantity:
        return "Order Fully Fulfilled"
    elif fulfilled > 0:
        return "Order Partially Fulfilled"
    else:
        return "Order Cannot Be Fulfilled"

inventory = {
    'item1': {'quantity': 10, 'price': 5},
    'item2': {'quantity': 5, 'price': 3},
    'item3': {'quantity': 7, 'price': 8}
}

print(can_fulfill_order(inventory, 10, 50))

