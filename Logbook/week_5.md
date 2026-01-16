# Introduction to Programming – Week 5  
**Scripts and Modules**

## Overview
This lab explained how Python programs are saved as **scripts** and organised using **modules**. We learned how scripts are run from the terminal, how command-line arguments work, and how Python finds and manages imported code. These ideas are important for building larger and reusable programs.

---

## Python Scripts
A Python script is a file that ends with `.py` and is run from the command line.

Unlike interactive mode, scripts do not show results automatically. Any output must be shown using `print()`. This helps programmers control what the program displays.

Scripts can be written in any text editor. While IDEs are helpful, they are not required.

---

## Running Scripts and Command-Line Arguments
Scripts are executed using the Python interpreter from the terminal. Extra information can be passed to a script when it runs using **command-line arguments**.

These arguments are stored in `sys.argv`:
- The first item is the script name  
- The remaining items are user-provided inputs  

This allows a program to change its behaviour without editing the code.

---

## Using the `sys` Module
The `sys` module gives access to system-related features.

By importing `sys`, programs can:
- Read command-line arguments  
- Check how many arguments were provided  

This helps prevent errors and makes programs more reliable.

---

## Importing Modules and Using Aliases
Python allows:
- Importing full modules  
- Importing specific functions or variables  
- Giving modules shorter names using aliases  

Importing only what is needed keeps code clean. Using `import *` is discouraged because it can cause confusion and name clashes.

---

## Symbol Tables and Names
Python keeps track of names using **symbol tables**. Each module has its own table, which helps avoid conflicts between variables and functions.

The `dir()` function can be used to see what names exist inside a module, which is useful for learning and debugging.

---

## Module Search Path
When a module is imported, Python searches through directories listed in `sys.path`. Knowing this helps when working with custom modules or fixing import errors.

---

## The `__name__` Variable
Python automatically sets the `__name__` variable.

- If the file is run directly, `__name__` is `"__main__"`  
- If the file is imported, `__name__` becomes the module name  

This allows certain code to run only when the file is executed as a script.

---

## Conclusion
This lab helped explain how Python programs are run and organised. By learning about scripts, modules, imports, and command-line arguments, we gained important skills for writing well-structured and reusable Python programs.
