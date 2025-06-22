# Function with *args: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    # sum = 0
    # for i in args:
    #     # print(i)
    #     sum += i
    # return sum

    #Method- 02
    return sum(args)


print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))