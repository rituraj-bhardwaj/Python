# write a program to display even numbers out of a list.


def is_even01(n):
    return n%2 == 0

is_even02 = lambda n : n%2 == 0

nums = [1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12]

evens01 = list(filter(is_even01, nums))
evens02 = list(filter(is_even02, nums))
evens03 = list(filter(lambda n: n%2 == 0, nums))

print(evens01)
print(evens02)
print(evens03)
