# Strings in Python

Strings are **immutable**, meaning once created, they cannot be changed.

---

## String Operations

| Operation     | Example           | Output      |
| ------------- | ----------------- | ---------- |
| Concatenation | `'Py' + 'thon'`   | `'Python'` |
| Repetition    | `'Hi' * 3`        | `'HiHiHi'` |
| Membership    | `'P' in 'Python'` | `True`     |
| Length        | `len('Python')`   | `6`        |

---

## Common String Methods

```python
text = "hello World"
text.lower()           # 'hello world'
text.upper()           # 'HELLO WORLD'
text.title()           # 'Hello World'
text.capitalize()      # 'Hello world'
text.strip()           # removes whitespace from both ends
text.replace("l", "*") # 'he**o Wor*d'
text.count("l")        # 3
text.find("World")     # 6
text.startswith("h")   # True
text.endswith("d")     # True


- String formatting
name = "Alice"
age = 25

f"Name: {name}, Age: {age}"           # f-string (recommended)
"Name: {}, Age: {}".format(name, age) # old style


- String splitting and joining
s = "apple,banana,grape"

s.split(",")             # ['apple', 'banana', 'grape']
" ".join(['a', 'b'])     # 'a b'


- Escape character
| Character | Meaning      |
| --------- | ------------ |
| `\n`      | New line     |
| `\t`      | Tab          |
| `\\`      | Backslash    |
| `\'`      | Single quote |
| `\"`      | Double quote |
