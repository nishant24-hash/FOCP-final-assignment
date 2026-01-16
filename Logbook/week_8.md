# Input and Output (I/O) & File Handling

---

## What this lesson is about
This lesson teaches the basics of **input and output (I/O)** and **working with files** in Python.

You will learn:
- How to **format output** nicely
- How to **read and write files**
- How to control file positions
- How to safely handle errors with files

---

## Input and Output (I/O)
All programs follow the pattern:
- **Input** → **Processing** → **Output**

So far, we have used:
- `input()` to get information
- `print()` to display information

I/O is not just for humans. It can also come from:
- **Files**
- **Networks**
- **Sensors**  
- **Other programs**

---

## Formatting Output
Python gives several ways to make output **look nice**:

### 1. F-strings (Python 3.6+)
- Add `f` before quotes and put variables in `{}`:

```python
print(f"Hello {name}, your balance is {balance:.2f}")  # shows 2 decimals
Align text/numbers:

# File Handling in Python

Python provides built-in support to read from and write to files, allowing programs to store data permanently or process large amounts of information. Files can be text files or binary files.

---

## Opening Files
Use the open() function to open a file:

file = open("example.txt", "r")  # "r" = read mode

Common modes:

- "r" – read (default)
- "w" – write (overwrites file if it exists)
- "a" – append (adds data to the end)
- "x" – create a new file; fails if it exists
- "b" – binary mode (use with other modes, e.g., "rb")
- "t" – text mode (default, e.g., "rt")

---

## Reading from Files
- read() – reads the whole file as a single string
- readline() – reads one line at a time
- readlines() – reads all lines into a list of strings

Example:

with open("example.txt", "r") as file:
    content = file.read()

> Using with ensures the file is automatically closed after use.

---

## Writing to Files
- write(string) – writes a string to the file
- writelines(list_of_strings) – writes multiple lines at once

Example:

with open("output.txt", "w") as file:
    file.write("Hello, world!\\n")

---

## Closing Files
- close() method closes the file
- Using with open() is preferred because it handles closing automatically, even if errors occur

---

## Other Useful File Operations
- seek(offset) – moves the cursor to a specific position
- tell() – returns the current position of the cursor
- truncate() – trims the file to the current cursor position

---

## File Handling Best Practices
- Always close files after use (or use with)
- Handle exceptions to prevent errors during reading/writing
- Use the appropriate mode for reading, writing, or appending
