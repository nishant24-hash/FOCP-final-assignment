# Introduction to Programming – Week 3  

## Overview
This lab taught how Python programs make choices and repeat actions. We learned about True/False (Boolean) conditions, comparison and logical operators, and using if, elif, and else to make decisions. We also learned about loops to repeat tasks, checking if items are in a list or string (membership testing), using the ternary operator for short decisions, and controlling loops with break and continue.

---

## Boolean Expressions
Boolean expressions always produce either `True` or `False`. They are mainly used in `if` statements and loops.

- Common comparison operators:  
  `<`, `>`, `<=`, `>=`, `==`, `!=`

These expressions usually involve variables and can compare numbers, strings, or other data types. Comparisons only work between compatible types; comparing different types can cause errors.

A common mistake happens when comparing user input directly, since `input()` returns a string by default.

---

## Logical Operators
Logical operators combine multiple conditions into one:

- `and` – True only if both conditions are True  
- `or` – True if at least one condition is True  
- `not` – Flips the result  

Using parentheses helps make conditions easier to read. Python also supports chained comparisons for cleaner logic.

---

## Membership Testing
Membership testing checks whether a value exists in a sequence like a string or list.

- `in` – checks if a value is present  
- `not in` – checks if a value is absent  

This is often simpler than writing long comparison expressions.

---

## The `if` Statement
The `if` statement allows code to run only when a condition is True.

- Indentation defines the code block
- Conditions are usually Boolean expressions
- Only the indented section runs if the condition is met

### `elif` and `else`
- `elif` checks additional conditions
- `else` runs when all previous conditions are False
- Only one block runs in an `if-elif-else` structure

Python also treats some values as Boolean:
- `0`, empty strings, and empty lists → `False`
- Non-zero values and non-empty sequences → `True`

Even so, clear Boolean conditions are recommended for better readability.

---

## Ternary Operator
The ternary operator is a short way to write an `if-else` statement in one line.

Syntax:
```python
value_if_true if condition else value_if_false
