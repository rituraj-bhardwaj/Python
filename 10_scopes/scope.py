
x = 10  # Global variable

def show():
    x = 5  # Local variable
    print("Local x:", x)

show()
print("Global x:", x)


def outer1():
    x = "enclosed"
    def inner():
        print("x from enclosing scope:", x)
    inner()

outer1()



# closure example
def outer2():
    msg = "Hello"

    def inner():
        print(msg)  # Remembers 'msg' even after outer() is done

    return inner

closure_func = outer2()
closure_func()


# scope modifier
x = 0

def update():
    global x
    x += 10

update()
print(x)
