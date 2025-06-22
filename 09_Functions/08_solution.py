# Function with **kwargs: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def fun_with_kargs(**kargs):
    for key, value in kargs.items():
        print(f"{key}: {value}")

fun_with_kargs(name='Rituraj')
fun_with_kargs(name='Rituraj', age=21, height=173)