"""
Problem:
Analyze text: count frequency of words excluding stopwords and efficiently query top-k frequent words starting with a prefix.
"""
from collections import defaultdict, Counter
import heapq
import re

STOPWORDS = {"the", "is", "at", "on", "in", "and", "a", "an", "to", "of"}

def preprocess(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if word not in STOPWORDS]

def analyze_text(text):
    words = preprocess(text)
    freq = Counter(words)
    return freq

def query_top_k(freq, prefix, k):
    filtered = [(word, count) for word, count in freq.items() if word.startswith(prefix)]
    return heapq.nlargest(k, filtered, key=lambda x: x[1])


text = "The quick brown fox jumps over the lazy dog. This is a test. The fox is quick."
freq = analyze_text(text)
print("Top 3 words starting with 'th':", query_top_k(freq, "th", 3))
