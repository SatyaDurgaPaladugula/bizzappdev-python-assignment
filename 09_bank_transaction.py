"""
Problem:
Track bank transactions and balance.
"""

def bank_analyzer(transactions):
    balance = 0
    for txn in transactions:
        if txn["type"] == "credit":
            balance += txn["amount"]
        elif txn["type"] == "debit":
            balance -= txn["amount"]
        print(f"After {txn['type']} of ₹{txn['amount']}, balance is ₹{balance}")
    print("Final Balance = ₹", balance)

transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 200},
    {"type": "credit", "amount": 500},
]
bank_analyzer(transactions)
