# Compute the factorial of a number using a while loop.

num = 5
fact = 1
i = num
while i>0:
    fact *= i
    i -= 1
print(fact)