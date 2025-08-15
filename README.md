# Thoughtful  
  
# 📦 Package Sorting Utility

This repository contains a Python function for sorting packages into **STANDARD**, **SPECIAL**, or **REJECTED** stacks based on their **dimensions**, **volume**, and **mass**.

## ✨ Features
- Validates and cleans numeric input (supports numbers as strings with optional spaces).
- Classifies packages according to **bulky** and **heavy** criteria.
- Handles invalid and negative inputs with clear error messages.
- Does **not** use ternary operators for classification logic.

---

## 📜 Function Definition

```python
def sort(width, height, length, mass):
    """
    Sort packages into STANDARD, SPECIAL, or REJECTED stacks based on volume, dimensions, and mass.
    
    :param width: Width of the package in cm
    :param height: Height of the package in cm
    :param length: Length of the package in cm
    :param mass: Mass of the package in kg
    :return: str - one of "STANDARD", "SPECIAL", "REJECTED"
    """
