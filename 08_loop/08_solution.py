# Check if a number is prime.

num = int(input("Enter a number: "))

divisorCount = 0

for each in range(2, num//2 + 1):
    if num%each == 0:
        divisorCount += 1

if divisorCount == 0:
    print("Given number is a prime number")
else:
    print("Given number is not a prime number")