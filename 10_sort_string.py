"""
Problem:
Separate letters and digits, sort each, and concatenate.
"""
def sort_string(s):
    letters = sorted([c for c in s if c.isalpha()])
    digits = sorted([c for c in s if c.isdigit()])
    return ''.join(letters + digits)

print(sort_string("B4A1D3"))  
