# 1_seating_arrangement.py
"""
Problem:
You have N guests attending a dinner party. Each guest has exactly two preferred neighbors they'd like to sit next to.
Determine a valid circular seating arrangement satisfying all preferences.
"""
from itertools import permutations

def is_valid_seating(seating, preferences):
    n = len(seating)
    for i in range(n):
        guest = seating[i]
        left_neighbor = seating[(i - 1) % n]
        right_neighbor = seating[(i + 1) % n]
        if not (left_neighbor in preferences[guest] and right_neighbor in preferences[guest]):
            return False
    return True

def find_seating_arrangement(preferences):
    guests = list(preferences.keys())
    for seating in permutations(guests):
        if is_valid_seating(seating, preferences):
            return seating
    return "No valid arrangement found"


guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

print("Seating Arrangement:", find_seating_arrangement(guests))
