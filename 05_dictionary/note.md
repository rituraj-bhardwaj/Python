# 📘 Python Dictionaries – Notes and Examples

## 🧾 What is a Dictionary?

A **dictionary** in Python is an unordered, mutable collection of key-value pairs. Each key must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any type.

```python
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
```

## 🛠 Creating Dictionaries
```python
# Using curly braces
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Using dict() constructor
user = dict(name="John", age=30)

# Empty dictionary
empty = {}
```

## 🔍 Accessing Elements
```python
print(car["brand"])         # Ford
print(car.get("model"))     # Mustang
print(car.get("color", "N/A"))  # N/A if key doesn't exist
```

## 📝 Modifying Dictionaries
```python
car["year"] = 2025              # Update value
car["color"] = "red"            # Add new key
del car["model"]                # Delete key
car.pop("brand")                # Delete using pop()
```

## 📚 Dictionary Methods
```python
d = {"a": 1, "b": 2, "c": 3}

d.keys()           # dict_keys(['a', 'b', 'c'])
d.values()         # dict_values([1, 2, 3])
d.items()          # dict_items([('a', 1), ('b', 2), ('c', 3)])
d.update({"d": 4}) # Adds new pair or updates existing
d.clear()          # Empties the dictionary
```

## 🔄 Iterating Through a Dictionary
```python
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key} => {value}")
```

## ✅ Dictionary Comprehensions
```python
squares = {x: x*x for x in range(5)}  # {0:0, 1:1, ..., 4:16}
```

## 📌 Nested Dictionaries
```python
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 22, "grade": "B"}
}

print(students["alice"]["grade"])  # A
```