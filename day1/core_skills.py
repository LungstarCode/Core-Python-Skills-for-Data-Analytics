# Data types
    # 1: Python Lists: Creation, indexing, slicing, list comprehensions, sorting, appending/removing elements.

#Example of a List and some operations

numbers = [3, 1, 6, 7, 8]
squared = [x**2 for x in numbers ] # list comprehension
squared.sort(reverse=True) # sorting the squared list in descending order
print(squared)