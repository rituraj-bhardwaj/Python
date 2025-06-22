# Polymorphism in Functions : Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# def multiply(num1: int, num2: int):
#     return num1 * num2

# def multiply(str1, str2):
#     return str1 + str2

# print(multiply(5, 6))

# print(multiply('Rituraj', 'Bhardwaj'))

# Method -02

def multiply(param1, param2):
    return param1 * param2

print(multiply(5, 5))
print(multiply('5', 5))
print(multiply(5, '5'))