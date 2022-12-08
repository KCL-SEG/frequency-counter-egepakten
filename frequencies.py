"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {}
    # Your code goes here
    for index in items:
        counter = 0
        for search_item in items:
            if isinstance(index, str):
                if str(index) == str(search_item):
                    counter+=1
                    frequencies[index] = counter
    return frequencies
