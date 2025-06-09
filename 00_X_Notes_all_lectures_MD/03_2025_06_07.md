---
title: Python Basics Lecture 3
author: PZA
date: 2025-03
tags: [python, logic, nested, boolean, conditions, education]
---

# 🐍 Python Basics (PB), Mar 2025  
## Lecture 3: Nesting, Logic & Boolean Expressions

---

## 📚 Table of Contents

- [🔁 Nested Structures](#-nested-structures)
- [🔗 Logical Operators](#-logical-operators)
- [🧠 Truth Tables](#-truth-tables)
- [💡 Short-Circuiting](#-short-circuiting)
- [✅ Pythonic Comparisons](#-pythonic-comparisons)
- [🚨 Common Mistakes](#-common-mistakes)
- [🔄 DRY & Clean Structure](#-dry--clean-structure)
- [🧱 Nestedness Limits](#-nestedness-limits)
- [🧩 Practice Questions](#-practice-questions)

---

## 🔁 Nested Structures

### 📌 Nested `if-elif-else`

You can nest one condition inside another:

```python
if condition_1:
    line_1
    line_2
    if condition_2:
        line_3
        line_4
elif condition_3:
    do_something_else()
else:
    handle_fallback()
```

> 💡 Only use nesting when absolutely needed — too much can make logic harder to follow.

---

## 🔗 Logical Operators

Python uses:

| Operator | Description           |
|----------|-----------------------|
| `and`    | True if both are true |
| `or`     | True if at least one is true |
| `not`    | Inverts a boolean     |

🚫 Python does **not** use `&&`, `||`, `!`  
✅ Use `and`, `or`, `not`

---

## 🧠 Truth Tables

### 🔹 `and`

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True ✅ |
| True  | False | False ❌ |
| False | True  | False ❌ |
| False | False| False ❌ |

### 🔹 `or`

| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True ✅ |
| True  | False | True ✅ |
| False | True  | True ✅ |
| False | False| False ❌ |

### 🔹 `not`

| A     | `not A` |
|-------|---------|
| True  | False ❌ |
| False | True ✅ |

---

## 💡 Short-Circuiting

- `or` stops at first `True`  
- `and` stops at first `False`

```python
print(True or False and False)  # and runs first → True or False → True
print((True or False) and False)  # parentheses change order → True and False → False
```

> 💡 Use parentheses `()` to clarify complex logic.

---

## ✅ Pythonic Comparisons

Instead of:
```python
if number > 50 and number < 60:
```

Use:
```python
if 50 < number < 60:
```

> 📏 Clean and readable: checks if number is in `(50, 60)` interval

---

## 🚨 Common Mistakes

- ❌ Using `=` instead of `==` in comparisons
- ❌ Over-nesting logic
- ❌ Forgetting to use parentheses in complex conditions
- ❌ Confusing `not` vs `!=`

> ⚠️ Be aware of **off-by-one** and **edge case** bugs!

---

## 🔄 DRY & Clean Structure

**DRY Principle**: *Don't Repeat Yourself*

- Avoid copying logic blocks
- Extract common logic into functions

> ✨ Apply **Separation of Concerns**: input, processing, and output should be clearly separated.

---

## 🧱 Nestedness Limits

Avoid more than **3 levels of nested `if` blocks**:

✅ OK:
```python
if ...:
    if ...:
        if ...:
            do_something()
```

🚫 Too deep:
```python
if ...:
        if ...:
                if ...:
                        if ...:
```

> 💡 Break into functions if logic gets too deep.

---

## 🧩 Practice Questions

### Q1: What is the output?

```python
print(not (True and False))
```

- a) True ✅  
- b) False  
- c) Error

---

### Q2: Which evaluates to `False`?

- a) `True and False` ✅  
- b) `True or False`  
- c) `not False`

---

### Q3: What will this print?

```python
num = 101
if num > 50 and num % 2 == 0:
    print("Even and large")
else:
    print("Not both")
```

- a) Even and large  
- b) Not both ✅  
- c) Error

---

### Q4: What is the correct way to check if a number is between 10 and 20?

- a) `10 < num and num < 20`  
- b) `num > 10 or num < 20`  
- c) `10 < num < 20` ✅  
- d) `num == 10 and 20`

---

### Q5: What is the result?

```python
print(True or (False and False))
```

- a) True ✅  
- b) False  
- c) None  
- d) Error

---

### Q6: Fix this nested block:
```python
if a > 0:
    if b > 0:
        print("A and B are positive")
    else
        print("B is not positive")
```

✅ Fixed:
```python
if a > 0:
    if b > 0:
        print("A and B are positive")
    else:
        print("B is not positive")
```

---

> ✅ End of Lecture 3 – Master nested logic, keep your code readable, and always think about logic flow!
