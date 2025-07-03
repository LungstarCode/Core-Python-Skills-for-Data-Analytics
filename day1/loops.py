# for loop 

prices = [5, 12, 8, 15, 9]
for x in prices:
    if x > 10:
        print(x) # results should be a 12 and 15

# while loop
numbers = [10, 20, 15, 30, 5]
total = 0
i = 0

while total <= 50 and i < len(numbers):
    total += numbers[i]
    i = i + 1

print(total)  # should be 75