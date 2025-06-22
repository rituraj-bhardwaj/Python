# Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


fruit = 'Banana'
colour = input("Enter colour of this fruit: ")

if colour.lower() == 'green':
    print("Unripe")
elif colour.lower() == 'yellow':
    print("Ripe")
elif colour.lower() == 'brown':
    print("Overripe")
else:
    print("Failed to determine")