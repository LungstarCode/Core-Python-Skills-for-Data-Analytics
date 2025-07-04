# A List in python is a datastructure that lets you store a collection of data in one variables, such as city names

cities = ["Joburg", "Mbombela", "Pretoria", "Polokwane", "Tzaneen"]

# getting an element of a list using indexing
cities[0] # Joburg 
cities[1] # Mbombela

# getting elements of a list using negative indexing
cities[-1] # last element - Tzaneen
cities[-2] # second last - Polokwane

# Slicing 
cities[1: -1] # exlude the first and last element
print(cities[1: -1])
print(cities[: -1]) # only exclude the last element

# Concatination and replication
cities + [ "Nelspruit", "Mathafin"]  # adding the list item to the existing cities list
cities = cities + [ "Nelspruit", "Mathafin"] 
print(cities)

cities_x2 = cities * 2 # repliactes the list 
print(cities_x2)