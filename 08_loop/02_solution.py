# Calculate the sum of even numbers up to a given number n.

n = 25
sum = 0
for each in range(1, n+1):
    if each%2 == 0:
        sum += each
print("Sum = ", sum)