# 📝 Python Lists – Notes and Examples

## 📌 What is a List?

A **list** in Python is a built-in data type that is a mutable, ordered sequence of elements. Lists can hold items of any type — integers, strings, other lists, etc.

## 🧩 Creating List
```python
empty_list = []
numbers = [1, 2, 3, 4]
mixed = [1, "hello", True, 3.14]
nested = [[1, 2], [3, 4]]
```

## 🔍 Accessing Elements
```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])      # apple
print(fruits[-1])     # cherry
print(fruits[1:3])    # ['banana', 'cherry']
```

## 🎯 Common List Operations
```python
| Operation     | Example                  | Result         |
| ------------- | ------------------------ | -------------- |
| Concatenation | `[1, 2] + [3, 4]`        | `[1, 2, 3, 4]` |
| Repetition    | `[1] * 3`                | `[1, 1, 1]`    |
| Membership    | `3 in [1, 2, 3]`         | `True`         |
| Length        | `len([1, 2, 3])`         | `3`            |
| Index         | `[10, 20, 30].index(20)` | `1`            |
```

## ✏️ Modifying Lists
```python
numbers = [1, 2, 3]

numbers[0] = 10
numbers.append(4)
numbers.pop()      # removes last
numbers.insert(1, 15)
numbers.remove(3)
del numbers[0]
```

## 📋 List Methods
```python
nums = [4, 1, 3, 2]

nums.sort()         # [1, 2, 3, 4]
nums.reverse()      # [4, 3, 2, 1]
nums.count(3)       # 1
nums.clear()        # []
```

## 🔄 Iterating Through a List
```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
```

## 🔧 List Comprehensions
```python
squares = [x ** 2 for x in range(5)]   # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]
odds = [x for x in range(10) if x % 2 == 1]
```