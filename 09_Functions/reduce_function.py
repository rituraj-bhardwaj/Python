

# The reduce() function in Python is used to apply a function cumulatively to the items of an iterable, reducing the iterable to a single value.

# reduce() is not a built-in function in Python 3. You need to import it from the functools module:

from functools import reduce

# Syntax: reduce(function, iterable_object)

# Sum of numbers:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = reduce(lambda a,b : a+b, nums)
print(sum)