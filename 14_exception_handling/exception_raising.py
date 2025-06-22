# Write a program that takes user input and based on input an exception will be raised if the input is a negative number, else the square root will be printed will be printed.


# custom exception class
class CustomError(Exception):
    pass


def squareRoot(num):
    if num < 0:
        raise CustomError("Number can't be negative")
    root = num ** (1/2)
    return round(root, 3)

try:
    num = int(input("Enter a number:"))
    square_root = squareRoot(num)
    print(f"square root of {num} = {square_root}")
except CustomError as e:
    print("ERROR:", e)
except ValueError as e:
    print("ValueError:", e)
except Exception:
    print("Something went wrong")
finally:
    print("Exiting program...")
