# 📙 Python Tuples – Notes and Examples

## 📌 What is a Tuple?

A **tuple** is an ordered, immutable collection of elements. Tuples are similar to lists, but they **cannot be modified** (no append, remove, etc.).

```python
coordinates = (10, 20)
```

## ✨ Creating Tuples
```python
t1 = (1, 2, 3)
t2 = ("apple", "banana")
t3 = ()                   # Empty tuple
t4 = (42,)                # Single-element tuple (note the comma)
t5 = tuple([1, 2, 3])     # Using the tuple() constructor
```

## 🔍 Accessing Elements
```python
colors = ("red", "green", "blue")

print(colors[0])      # red
print(colors[-1])     # blue
print(colors[1:])     # ('green', 'blue')
```

## ♻️ Tuple Operations
```python
| Operation     | Example          | Output            |
| ------------- | ---------------- | ----------------- |
| Length        | `len(t1)`        | 3                 |
| Concatenation | `(1, 2) + (3,)`  | `(1, 2, 3)`       |
| Repetition    | `("A",) * 3`     | `('A', 'A', 'A')` |
| Membership    | `2 in (1, 2, 3)` | `True`            |
```

## 🔁 Iterating Over Tuples
```python
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)
```

## 🧩 Tuple Unpacking
```python
point = (3, 5)
x, y = point

print(x)  # 3
print(y)  # 5
```

## 📚 Tuple Methods
```python
t = (1, 2, 3, 2, 1)

t.count(2)       # 2
t.index(3)       # 2
```

## 🎯 Nested Tuples
```python
matrix = ((1, 2), (3, 4))

print(matrix[1][0])   # 3
```