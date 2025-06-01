---
title: Python Basics Lecture 6
author: PZA
date: 2025-03
tags: [python, nested-loops, problem-solving, dry, education]
---

# 🐍 Python Basics (PB), Mar 2025  
## Lecture 6: Nested Loops, Loop Patterns & Problem Solving

---

## 📚 Table of Contents

- [🔁 Combining Concepts](#-combining-concepts)
- [🔂 Nested Loop Structure](#-nested-loop-structure)
- [🧠 Common Techniques](#-common-techniques)
- [🧮 Problem Decomposition](#-problem-decomposition)
- [📏 Percentage Calculations](#-percentage-calculations)
- [🧱 Deep Nesting Patterns](#-deep-nesting-patterns)
- [🧼 DRY & Bugs Awareness](#-dry--bugs-awareness)
- [🧩 Practice Questions](#-practice-questions)

---

## 🔁 Combining Concepts

### ✅ Concept 1: Nestedness  
### ✅ Concept 2: Loops (for & while)

We can **combine both** to solve complex tasks using **nested loops**.

---

## 🔂 Nested Loop Structure

```python
for outer in outer_collection:
    outer_logic_1

    for inner in inner_collection:
        inner_logic

    outer_logic_2
```

You can nest any combination:
- `for` inside `for`
- `for` inside `while`
- `while` inside `for`, etc.

---

## 🧠 Common Techniques

### 1️⃣ `break` for nested loops → use flag variables

```python
found = False

for i in range(5):
    for j in range(5):
        if i + j == 6:
            found = True
            break
    if found:
        break
```

> 💡 Use `found` flag to break multiple levels cleanly.

---

### 2️⃣ Looping through digits of a number

```python
num = 9876
for digit in str(num):
    print(digit)   # prints '9', '8', '7', '6'
```

> 🧠 Convert to string for digit-wise iteration.

---

### 3️⃣ Using `enumerate()`

```python
text = "hello"
for index, char in enumerate(text):
    print(index, char)
```

> ✅ `enumerate()` gives you both index and element.

---

## 🧮 Problem Decomposition

To solve complex problems:

1. Start with a **skeleton** or outline  
2. Identify **smaller subtasks**  
3. Tackle one simple task at a time

---

### 🧪 Example Subproblem: Check if a number is prime

```python
is_prime = True
n = 29

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
```

---

## 📏 Percentage Calculations

Understanding percent logic is key in math-based tasks:

```python
x = 6
print(x * 100)      # → 600
print(5 * 6)        # → 30
print(100 + 5)      # → 105
```

> ⚠️ Be careful with floating-point division and rounding if needed.

---

## 🧱 Deep Nesting Patterns

You might encounter heavy nesting in problems:

### 6.1: 4-level nested `for` loops

```python
for a in range(...):
    for b in range(...):
        for c in range(...):
            for d in range(...):
                do_something()
```

### 6.2: `while` containing `for`

```python
while some_condition:
    for x in range(...):
        do_something()
```

> ⚠️ Watch for **loop depth** → refactor if it's hard to follow.

---

## 🧼 DRY & Bugs Awareness

### 🧹 DRY → Don’t Repeat Yourself

- Avoid copy-pasting blocks  
- Extract repeated logic into **functions**

### 🐞 Think About:
- ❗ Missed cases  
- ⚠️ Edge cases  
- 🔁 Off-by-one mistakes  
- ✅ Inputs that just pass/fail conditions

---

## 🧩 Practice Questions

### Q1: What does this print?

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

- a) All combinations from 0 to 2 ✅  
- b) Only (0, 0), (1, 1)  
- c) Error

---

### Q2: Which is the cleanest way to iterate through digits of `5432`?

- a) `for i in 5432`  
- b) `for digit in str(5432):` ✅  
- c) `for digit in list(5432)`  
- d) `for digit in range(5432)`

---

### Q3: What does `enumerate("cat")` yield?

```python
for i, c in enumerate("cat"):
    print(i, c)
```

- a) 0 c 1 a 2 t  
- b) 0 c, 1 a, 2 t ✅  
- c) 1 c, 2 a, 3 t  
- d) Error

---

### Q4: Which loop uses a `flag` to break nested loops?

```python
found = False
for i in range(3):
    for j in range(3):
        if i == j:
            found = True
            break
    if found:
        break
```

- a) breaks outer loop ✅  
- b) continues loop  
- c) error  
- d) doesn't stop

---

### Q5: How many times will this run?

```python
count = 0
for i in range(2):
    for j in range(3):
        count += 1
print(count)
```

- a) 3  
- b) 5  
- c) 6 ✅  
- d) 9

---

> ✅ End of Lecture 6 – Use nested loops wisely, decompose your problems, and always check your assumptions!
