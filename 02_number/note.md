# Numbers in Python

- types of numbers : int, float, complex
- type checking : type(data_type)
- type conversion : int(3.9), float(5), complex(4)
- Arithematic operation : +, -, *, /(float division), //(floor division), %, **(exponential)

- Boolean : 
1. (True == 1) = True -> True is considered as 1 in terms of value
2. (True == 2) = False
3. (False + True) = 1
4. (False - True) = -1

- Build in functions : 
1. abs(x) -> absolute value => abs(-7) = 7
2. pow(x, y) -> (same as x ** y)
3. round(x) -> round to nearest integer => round(3.6) = 4
4. max(x, y, z) -> max of values => max(1, 2, 3) = 3
5. min()

- Math module : import math
1. math.sqrt(16) = 4.0 => float answer
2. math.ceil(3.2) = 4, math.ceil(-3.2) = -3
3. math.floor(3.2) = 3, math.floor(-3.2) = -4
4. math.pi = 3.141592653....

- Random Module : import random
1. random.random() => random float [0.0, 1.0)
2. random.randint(1, 10) => random integer from 1 to 10
3. random.choice([1, 2, 3, 4, 5]) => any randomly choosen item

- Decimal and Fraction modules : (import decimal from Decimal) & (import fractions from Fraction)
1. Decimal('0.1') + Decimal('0.2')
2. Fraction(1, 3) + Fraction(1, 6)


