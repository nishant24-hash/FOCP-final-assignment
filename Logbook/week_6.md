# Introduction to Programming – Week 6  
**Lists, List Comprehensions & Tuples**

---

## Working with Lists
Lists are **mutable collections** that can store multiple items. They support indexing, slicing, concatenation, and looping.

### Common List Methods
**To change lists:**
- `append(value)` – Add one item at the end  
- `extend(iterable)` – Add multiple items from another list or iterable  
- `insert(index, value)` – Insert an item at a specific position  
- `remove(value)` – Remove first occurrence of a value  
- `pop([index])` – Remove and return last item (or a specific index)  
- `clear()` – Remove all items  
- `sort([key=func, reverse=True/False])` – Sort items, optionally by a function or in reverse  
- `reverse()` – Reverse the order of items  

**To get information from lists:**
- `index(value, [start, end])` – Find the position of a value  
- `count(value)` – Count how many times a value appears  
- `copy()` – Make a shallow copy of the list  

You can also use `del` to delete items by index, remove slices, or delete the whole list variable.

---

## List Comprehensions
List comprehensions provide a **short and readable way** to create lists using a single line.

Example:
```python
squares = [x*x for x in range(10)]
