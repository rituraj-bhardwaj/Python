# Write a generator function that yields even numbers up to a specified limit.

def even_generator(num):
    for i in range(2, num+1, 2):
        yield i

for i in even_generator(20):
    print(i)