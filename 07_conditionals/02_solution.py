# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter age: "))
day = 'Monday'

# if day == 'Wednesday':
#     if age < 18:
#         print("Ticket price is $6")
#     else:
#         print("Ticket price is $10")
# else:
#     if age < 18:
#         print("Ticket price is $8")
#     else:
#         print("Ticket price is $12")

price = 12 if age > 18 else 8
price = price - 2 if day == 'Wednesday' else price

print("Ticket price is ", price)