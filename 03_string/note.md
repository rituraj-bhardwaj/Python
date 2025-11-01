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
text.title()           # 'Hello World' => every word first letter capital
text.capitalize()      # 'Hello world' => first letter of a sentence is capitalized
text.strip()           # removes whitespace from both ends
text.replace("l", "*") # 'he**o Wor*d'. Original text remains unchanged, it makes changes and return modified text.
text.count("l")        # 3
text.find("World")     # 6 => Returns index of word or character if found, else -1 if not found.
text.startswith("h")   # True => Checks if text starts with the specified character or word.
text.endswith("d")     # True => Checks if text ends with the specified character or word.


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
