# calculate the area of a rectangle with width 7 and height 3
w = 7
h = 3
area = w*h
print('area of rectangle : ', area)

# convert celsius to fahrenheit (F = C * 9/5 + 32) for c = 37
c = float(37)
f = c*(9/5) + 32
print('Farhenheit equivalent to 37 c : ', f)

# type conversion : convert "45.67" into a float and integer
str = "45.67"
intValue = int(str)
floatValue = float(str)
print('int value : ', intValue, '\nfloat value : ', floatValue)

# Define z = 4 + 5j and print real and imaginary part
complex = 4 + 5j
print(complex.real)
print(complex.imag)

# Compute the cube root of 27 using exponentiation.
a = float(27)
b = a ** (1/3)
d = pow(a, 1/3)
print('cube root of 27 : ', b, d)

# Show the difference between round(3.75), math.floor(3.75), and math.ceil(3.75).
import math
print(round(3.75))
print(math.ceil(3.75))
print(math.floor(3.75))


# Find the sine of 90 degrees. (Hint: convert to radians first.)
print('sine of 90 degree : ', math.sin(math.pi/2))


# Generate a random integer between 50 and 100, and a random float between 0 and 1.
import random
print('random integer between 50 and 100 : ', random.randint(50, 100))
print('random float between 50 and 100 : ', float(random.randint(50, 100)))


# Given (x1, y1) and (x2, y2), write a function to compute the Euclidean distance.
x1 = 2
y1 = 4
x2 = 3
y2 = 6
distance = (((y2 - y1) ** 2) + ((x2 - x1) ** 2)) ** 1/2
print('Euclidean distance : ', distance)


# Write a function to solve a quadratic equation ax^2 + bx + c = 0 using the quadratic formula.

