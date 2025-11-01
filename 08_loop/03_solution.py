# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter a positive number: "))

for turn in range(1, 10+1):
    if turn == 5:
        continue
    print(turn*number)