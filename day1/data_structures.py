# Data types
    # 1: Python Lists: Creation, indexing, slicing, list comprehensions, sorting, appending/removing elements.

#Example of a List and some operations

numbers = [3 , 5, 6, 7, 8, 9]
squared = [x**2 for x in numbers] # List comprehension to square each item in the list
squared.sort(reverse=True) # sort the numbers in squared in descending order
print(squared)

# 2: Dictionary :Create a dictionary to store sales data (e.g., {"apple": 10, "banana": 15}) and write a function to calculate the total sales. Add a new item and update an existing one.

sales = {"Apple": 10 , "Banana": 15}
sales['Apple'] += 5
sales['Banana'] += 5
sales['Oranges'] = 30
total = sum(sales.values())  # adding all values in the dictionary
print(total)

# 3. Tuples: Store a dataset record as a tuple (e.g., (name, age, salary)) and unpack it into variables for printing.

record = ("Lungile", 25 , 45000)
name, age, salary = record
print(f'name : {name}, age : {age} and salary is {salary} ')

# 4:  Sets: Remove duplicates from a list of product IDs using a set

product_ids = [101, 607, 567, 101, 101, 209, 567, 568]
ids = set(product_ids)
print(ids)  # Output should be {101, 607, 567, 209, 568}