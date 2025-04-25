"""
Problem:
Calculate slab-wise electricity bill.
"""
def calculate_bill(units):
    slabs = [(100, 5), (200, 7), (200, 10), (float('inf'), 15)]
    cost = 0
    remaining = units
    bill_details = []

    for limit, rate in slabs:
        use = min(remaining, limit)
        slab_cost = use * rate
        bill_details.append((use, rate, slab_cost))
        cost += slab_cost
        remaining -= use
        if remaining <= 0:
            break

    for use, rate, slab_cost in bill_details:
        print(f"{use} units @ {rate}/unit = ₹{slab_cost}")
    print("Total Amount Payable = ₹", cost)

calculate_bill(450)
