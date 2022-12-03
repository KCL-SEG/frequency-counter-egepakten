"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        counter = 1
        for search_item in items:
            if item == search_item:
                frequencies[item] = counter
                counter+=1
    return frequencies


#print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))
