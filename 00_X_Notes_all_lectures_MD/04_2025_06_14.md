---
title: Python Basics Lecture 4
author: PZA
date: 2025-03
tags: [python, for-loop, range, strings, beginner, education]
---

# 🐍 PBasics Python (PZA, Mar 2025)  
## Lecture 4: `for` Loops, `range()`, Indexing & DRY

---

## 📚 Table of Contents

- [🔁 `for` Loop Basics](#-for-loop-basics)
- [🔢 `range()` Usage](#-range-usage)
- [🛑 `break` and `continue`](#-break-and-continue)
- [📜 String Indexing](#-string-indexing)
- [🔢 Negative Indexing](#-negative-indexing)
- [📐 `for-else` Construct](#-for-else-construct)
- [🧠 DRY Principle](#-dry-principle)
- [🧩 Practice Questions](#-practice-questions)

---

## 🔁 `for` Loop Basics

### Base structure:
```python
for el in collection:
    ...
```

### Examples:

#### 1️⃣ Loop through string characters:
```python
for char in 'some_string':
    print(char)
```

#### 2️⃣ Loop using `range()`:
```python
for i in range(5):
    print(i)
```

---

## 🔢 `range()` Usage

### Syntax:
```python
range(start, stop, step)
```

- `[start; stop)` → stop is **exclusive**
- Default: `start=0`, `step=1`

### Examples:

```python
range(4)          # → [0, 1, 2, 3]
range(1, 10)      # → [1, 2, ..., 9]
range(1, 25, 3)   # → [1, 4, 7, ..., 22]
```

> 💡 We count from `0` in programming

---

### Edge Case Examples:

```python
range(1, 10, 3)     # → [1, 4, 7]
range(1, 10, 77)    # → [1]
range(100, 10, 5)   # → []
range(10, 29, -5)   # → []
range(39, 29, -5)   # → [39, 34]
```

> ⚠️ If `step` doesn't move toward `stop`, the range is empty.

---

## 🛑 `break` and `continue`

- `break` → exits the entire loop  
- `continue` → skips to the next iteration

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## 📜 String Indexing

```python
text = "I am feeling good"

print(len(text))   # → 17
print(text[2])     # → 'a'
```

---

## 🔢 Negative Indexing

```python
name = "Peter"

print(name[0])      # → 'P'
print(name[-1])     # → 'r'
print(name[len(name) - 1])  # also → 'r'
```

Index diagram:

```
 P   e   t   e   r
 0   1   2   3   4
-5  -4  -3  -2  -1
```

---

## 📐 `for-else` Construct

```python
for item in items:
    if item == target:
        break
else:
    print("Not found")
```

> 💡 `else` runs **only if `for` loop does not break**

---

## 🧠 DRY Principle

**DRY** = *Don’t Repeat Yourself*

- Avoid repeating logic or blocks  
- Write reusable code (functions, variables)  
- Helps avoid bugs and keeps code clean

---

## 🧩 Practice Questions

### Q1: What does this output?

```python
for i in range(1, 10, 3):
    print(i)
```

- a) 1 4 7 ✅  
- b) 1 2 3  
- c) 1 3 6

---

### Q2: What's the output?

```python
word = "Python"
print(word[-2])
```

- a) `o` ✅  
- b) `n`  
- c) `t`

---

### Q3: What’s the length of `"Hello world"`?

```python
text = "Hello world"
print(len(text))
```

- a) 10  
- b) 11 ✅  
- c) 12

---

### Q4: Which `range()` generates `[3, 6, 9]`?

- a) `range(3, 10, 3)` ✅  
- b) `range(3, 9, 3)`  
- c) `range(3, 9)`

---

### Q5: Fix this loop:

```python
for i in range(5)
    print(i)
```

✅ Fixed:
```python
for i in range(5):
    print(i)
```

---

### Q6: Print even numbers from 2 to 10:

```python
for i in range(2, 11, 2):
    print(i)
```

---

### Q7: What's the last character in this string?

```python
msg = "Python"
print(msg[len(msg) - 1])
```

- a) P  
- b) n ✅  
- c) Error

---

> ✅ End of Lecture 4 – Loops are essential; master their flow and off-by-one details!
