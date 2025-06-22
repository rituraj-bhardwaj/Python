import fibo

fibo.fib(100)   #using fib() function defined in 'fibo.py' file
result = fibo.fib2(100)
print(result)

file_name = fibo.__name__
print(file_name)


# Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables

# There is a variant of the import statement that imports names from a module directly into the importing module’s namespace. For example:

from fibo import fib, fib2
fib(500)

# There is even a variant to import all names that a module defines:
from fibo import *


# If the module name is followed by as, then the name following as is bound directly to the imported module.
import fibo as fibonacci
fibonacci.fib(200)