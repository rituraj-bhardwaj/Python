# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 17

for each in range(1, 10+1):
    if each == 5:
        continue
    print(each*number)