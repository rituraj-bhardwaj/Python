# write a function that takes two input from user and prints its division. Use exception handling to handle 'devision by zero' exception and 'invalid input' error


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    div = round((num1/num2), 2)

    print(f"{num1}/{num2} = {div}")
    
except ZeroDivisionError as e:
    print(type(e))
    print("EXCEPTION:", e)

except ValueError as e:
    print(type(e))
    print("INVALID_INPUT:", e)

except Exception as e:
    print(type(e))
    print("Something went wrong!")

finally:
    print("Exiting program...")