# Introduction to Programming – Week 4  

## Overview
This lab explored how **functions** are used in Python to organise code and avoid repetition. The session covered using functions from modules, creating your own functions, adding documentation, working with different types of arguments, and using lambda expressions. These ideas help make programs clearer and easier to maintain.

---

## Importing and Using Functions
Python comes with many **built-in functions** like `print()` and `input()`. Extra functions are stored in **modules**, which must be imported before use.

Common import methods:
- `import module_name` – imports the whole module  
- `from module_name import function` – imports specific functions  
- `from module_name import *` – imports everything (generally avoided)

The **math** module was used to access functions like `sqrt()` and `log2()`, as well as constants such as `pi`.

---

## Defining Functions
Functions are created using the `def` keyword, followed by:
- A function name  
- Parameters inside parentheses  
- An indented code block  

Functions allow the same code to be reused many times. Parameters inside a function are **local**, meaning they only exist within that function.

---

## Docstrings and Documentation
Functions should include **docstrings**, written as triple-quoted strings at the start of the function.

- Explain what the function does  
- Can be viewed using `help()`  
- Make code easier to understand and update  

---

## Returning Values
Functions can send results back using `return`.

- `return` ends the function immediately  
- If no value is returned, Python returns `None`  
- Returned values can be saved or used directly  

---

## Default Arguments
Functions can have **default values** for parameters.

- Allows some arguments to be optional  
- Default parameters come after required ones  
- If no value is given, the default is used  

This makes functions simpler to call.

---

## Keyword Arguments
Functions can also be called using **parameter names**.

- Order does not matter  
- Required arguments must still be included  
- Positional arguments must come first  

This improves readability, especially with many parameters.

---

## Arbitrary Length Argument Lists
Functions can accept any number of arguments using `*args`.

- All values are stored in a tuple  
- Useful when the number of inputs is unknown  
- Common in calculations and summaries  

These arguments are usually placed at the end.

---

## Lambda Expressions
Lambda expressions create **short, unnamed functions** in one line.

Syntax:
```python
lambda parameters : expression
