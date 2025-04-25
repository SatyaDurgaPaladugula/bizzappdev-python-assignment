"""
Problem:
Print 1000 to 1 using recursion only (no loops).
"""
def reverse_count(n):
    if n == 0:
        return
    print(n)
    reverse_count(n - 1)

reverse_count(1000)




