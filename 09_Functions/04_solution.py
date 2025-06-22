# Function Returning Multiple Values: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    # return [area, circumference]
    return area, circumference


# [area, circumference] = circle(25)
area, circumference = circle(5)

print("Area:", round(area, 2), " circumference:", round(circumference, 2))