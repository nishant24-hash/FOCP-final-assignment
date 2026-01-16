# Introduction to Programming – Week 7  
**Sets and Dictionaries**

---

## Understanding Sets
Sets are **unordered collections of unique items**, meaning that each element appears only once and the order of items does not matter.  

### Key Characteristics:
- **Immutable elements:** Items inside a set must be of immutable types such as numbers, strings, or tuples. Lists or other sets cannot be directly added as elements.  
- **Mutable container:** The set itself can be changed; you can add or remove elements after it is created.  
- **No indexing or slicing:** Because sets are unordered, you cannot access elements by position.  
- **Fast membership testing:** Checking whether an item exists in a set (`in`) or does not exist (`not in`) is faster than with lists.  

### Creating Sets
Sets can be created in two main ways:

1. Using **curly braces `{}`** for simple, predefined elements:
```python
vowels = {"a", "e", "i", "o", "u"}

2. Using the set() constructor
```python
names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])

### Common Set Operations
-**Some important operations that can be performed on sets include:

- add(element) – Adds a new element to the set
- remove(element) – Removes an element; raises an error if not found
- discard(element) – Removes an element; does not raise an error if missing
- union() – Combines two sets
- intersection() – Finds common elements
- difference() – Finds elements in one set but not the other
- symmetric_difference() – Elements in either set but not both
