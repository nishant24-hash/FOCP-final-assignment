# Introduction to Programming – Week 2  

## Overview
This lab continued from Week 1 and focused on how Python stores and works with data. We learned about variables, data types, built-in functions, strings, indexing and slicing, and an introduction to lists. These ideas are important for writing clear and useful Python programs.

---

## Working with Variables
Variables are used to store data so it can be used later in a program. Each variable has a name chosen by the programmer.

Basic rules for variable names:
- Must start with a letter or underscore
- Can include letters, numbers, and underscores
- Are case-sensitive (`age` and `Age` are different)
- Should be clear and meaningful

Variables are created using the **assignment operator (`=`)**. A variable must have a value before it can be used.

---

## Assignment and Augmented Assignment
Python first evaluates the expression on the right side before assigning it to a variable.

**Augmented assignment operators** provide a shorter way to update values:
- `+=`, `-=`, `*=`, `/=`

These make code shorter and easier to read.

---

## Data Types
Every value in Python has a data type, which affects how it behaves.

Common data types:
- `int` – whole numbers  
- `float` – decimal numbers  
- `bool` – `True` or `False`  
- `str` – text  

Python uses **dynamic typing**, meaning a variable’s type can change while the program runs. The `type()` function is used to check data types.

Operators behave differently depending on data type, such as:
- `+` for adding numbers
- `+` for joining strings
- `*` for repeating strings

---

## Built-in Functions
Python includes many built-in functions for common tasks.

Functions are used by writing their name followed by parentheses.

Examples used:
- `print()` – shows output  
- `len()` – finds length  
- `type()` – shows data type  
- `input()` – gets user input  

Some functions return values that can be stored or used in expressions. Functions can also be nested.

---

## User Input and Type Conversion
The `input()` function always returns a string. This can cause problems when doing math.

To fix this, type conversion functions like `int()` were used to change input into numbers before calculations.

---

## Strings and Quotes
Strings can be written using:
- Single quotes (`' '`)
- Double quotes (`" "`)
- Triple quotes (`""" """`)

Using different quotes helps include quotes inside strings.

### Escape Sequences
Special characters are written using escape sequences:
- `\n` – new line  
- `\t` – tab  
- `\\` – backslash  
- `\"` and `\'` – quotes  

### Triple-Quoted Strings
Triple quotes allow multi-line text and make it easier to include quotes. They are often used for long text or documentation.

---

## Indexing and Slicing
Strings are sequences, so their characters can be accessed.

### Indexing
- Starts from 0  
- Accesses one character  
- Negative indexing counts from the end  

### Slicing
- Extracts part of a string  
- Format: `[start:end]`  
- Start is included, end is excluded  
- Missing or out-of-range values do not cause errors  

---

## Introduction to Lists
Lists store multiple values and are written using square brackets.

Key features:
- Ordered collection  
- Can have duplicate values  
- Support indexing and slicing  
- Support `+` and `*` operators  

Lists can hold different data types, but usually store similar values.

---

## Mutable and Immutable Types
- **Strings are immutable**: they cannot be changed  
- **Lists are mutable**: their values can be modified  

List items can be changed using indexing, slicing, or `append()`. Using `+=` changes the list directly, while normal `+` creates a new list.

---


