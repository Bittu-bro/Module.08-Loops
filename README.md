# Module 08 - Loops in Python 🔄

This module covers the fundamentals of **Loops in Python**.

In this module, I learned how to use `for` loops, `while` loops, the `range()` function, `break`, `continue`, nested loops, and loops with strings, lists, and dictionaries.

I also practiced loops through different exercises and small projects such as a dice roll program and a number guessing game.

---

## 📚 Topics Covered

- `for` loop
- `while` loop
- `range()` function
- Loops with strings
- Loops with dictionaries
- `break` statement
- `continue` statement
- Infinite `while` loop
- Nested loops
- Star patterns using loops
- `random` module
- Lists and loops
- Dictionaries and loops
- Practical exercises
- Number Guessing Game

---

# 📂 Files and Description

## 01. for loop.py

This file introduces the basic concept of the **`for` loop** in Python.

### Concepts:
- Basic `for` loop syntax
- Iterating through a sequence
- Repeating a block of code
- Loop variable

---

## 02. For loops with strings and dict.py

This file demonstrates how `for` loops can be used with **strings and dictionaries**.

### Concepts:
- Iterating through characters of a string
- Iterating through dictionary keys
- Working with dictionary data using loops

---

## 03. The range function.py

This file covers the **`range()` function** and its use with loops.

### Concepts:
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`
- Using `range()` with `for` loops
- Controlling the number of loop iterations

---

## 04. Total, highest and lowest using for loop.py

This file demonstrates how a `for` loop can be used to process multiple numbers and find useful results.

### Concepts:
- Iterating through numbers
- Calculating total
- Finding the highest value
- Finding the lowest value
- Using variables inside loops

---

## 05. continue and break.py

This file explains two important loop control statements: **`continue`** and **`break`**.

### Concepts:
- `break` statement
- `continue` statement
- Skipping an iteration
- Stopping a loop
- Controlling loop execution

---

## 06. The while loop.py

This file introduces the **`while` loop**.

### Concepts:
- Basic `while` loop syntax
- Condition-based repetition
- Updating a variable inside a loop
- Controlling when a loop should stop

---

## 07. Infinite while loop.py

This file demonstrates the concept of an **infinite `while` loop**.

### Concepts:
- Infinite loops
- Loop conditions
- Why a loop can continue indefinitely
- Controlling and stopping loops

---

## 08. random module.py

This file introduces Python's built-in **`random` module**.

### Concepts:
- Importing a module
- Using `random`
- Generating random values
- `random.randint()`

The `random` module is later used in the Number Guessing Game.

---

## 09. Nested loops.py

This file covers **nested loops**, where one loop is placed inside another loop.

### Concepts:
- Nested `for` loops
- Outer loop
- Inner loop
- Multiple levels of iteration
- Using nested loops for repeated patterns

---

## 10. Star pattern using for loops.py

This file uses `for` loops to create **star patterns**.

### Concepts:
- Nested `for` loops
- Repetition
- Controlling rows and columns
- Pattern printing
- Practical use of nested loops

---

# 📝 Exercises

## 11. Exercise - Roll a dice.py

This exercise demonstrates how the `random` module can be used to simulate a **dice roll**.

### Concepts:
- `random` module
- `random.randint()`
- Generating random numbers
- Basic Python logic

---

## 12. Exercise - List & Loops.py

This exercise combines **lists and loops**.

### Concepts:
- Creating and working with lists
- Iterating through list elements
- Using `for` loops with lists
- Processing list data

---

## 13. Exercise - Loops & dictionaries.py

This exercise combines **loops and dictionaries**.

### Concepts:
- Working with dictionaries
- Iterating through dictionary data
- Accessing dictionary keys and values
- Using loops with dictionaries

---

# 🎮 Mini Project

## 14. Number guessing game - problem.py

This file contains the **problem statement** for the Number Guessing Game.

The task is to create a game where the computer generates a secret number and the user tries to guess it within a limited number of attempts.

### Main requirements:
- Generate a random number
- Allow the user to enter guesses
- Give higher/lower hints
- Limit the number of attempts
- Check whether the guess is correct

---

## 15. Number guessing game - solution.py

This file contains the completed solution for the **Number Guessing Game**.

The program generates a random number between **1 and 50** and gives the user **10 attempts** to guess it.

### Concepts Used:
- `random` module
- `random.randint()`
- `while` loop
- `if-else`
- Nested conditions
- `break`
- User input
- Type casting
- Comparison operators
- Variables
- f-strings

### Game Logic:

1. A secret number is generated between 1 and 50.
2. The player gets 10 attempts.
3. The player enters a guess.
4. The program compares the guess with the secret number.
5. If the guess is correct, the game ends.
6. If the guess is smaller, the program gives a **Try Higher** hint.
7. If the guess is bigger, the program gives a **Try Lower** hint.
8. If all attempts are exhausted, the game ends.

---

# 🧠 What I Learned in This Module

After completing this module, I practiced how to:

- Use `for` loops
- Use `while` loops
- Work with the `range()` function
- Iterate through strings
- Iterate through lists
- Iterate through dictionaries
- Use `break` and `continue`
- Understand infinite loops
- Create nested loops
- Create patterns using loops
- Generate random numbers
- Combine loops with conditions
- Build small Python programs using loops
- Build a simple interactive game

---

# 📁 Project Structure

```text
Module 08 (Loops)
│
├── 01. for loop.py
├── 02. For loops with strings and dict.py
├── 03. The range function.py
├── 04. Total, highest and lowest using for loop.py
├── 05. continue and break.py
├── 06. The while loop.py
├── 07. Infinite while loop.py
├── 08. random module.py
├── 09. Nested loops.py
├── 10. Star pattern using for loops.py
├── 11. Exercise - Roll a dice.py
├── 12. Exercise - List & Loops.py
├── 13. Exercise - Loops & dictionaries.py
├── 14. Number guessing game - problem.py
├── 15. Number guessing game - solution.py
└── README.md