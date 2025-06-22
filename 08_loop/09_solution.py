# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate. items = ["apple", "banana", "orange", "apple", "mango"]

items = ["banana", "orange", "apple", "mango", "apple"]

length = len(items)
duplicate = False
for i in range(0, length):
    for j in range(i+1, length):
        if items[i] == items[j]:
            print("Duplicate in list: ", items[i])
            duplicate = True
            break
    if duplicate:
        break


# Method - 02
unique_values = set()

for item in items:
    if item in unique_values:
        print("Diplicate item: ", item)
        break
    unique_values.add(item)
