# 1. Write a Python program to apply the map() function to square a list of numbers.
def square(x):
    return x * x
num = [1, 2, 3, 4, 5]
sqr_num = list(map(square, num))
print(sqr_num)

# 2. Write a Python program that uses reduce() to find the product of a list of numbers.
from functools import reduce
def multiply(x, y):
    return x * y
num = [1, 2, 3, 4, 5]
product = reduce(multiply, num)
print(product)

# 3. Write a Python program that filters out even numbers using the filter() function.
def is_odd(n):
    return n % 2 != 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = list(filter(is_odd, num))
print(odd_num)