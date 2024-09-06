
# Field Validation

This document outlines a system for validating attributes of a class before they are set.

## Requirements

1. **Numerical Fields:** Must be integers within a specified range (minimum, maximum).
2. **Character Fields:** Must be strings within a specified length range (minimum, maximum).
3. **Simplification:** For this exercise, we'll assume classes don't use slots (simplifies attribute access using `__dict__`).
4. **Refactoring:** Implement a base `Validator` class and derive both `IntegerValidator` and `CharValidator` from it.
5. **Testing:** Provide comprehensive unit tests.

## Implementation Approach

1. **File Structure:**
   ```bash
   touch validatorsV1.py README.md testsV1.py 
   ```

2. **`IntegerValidator` Class:**
   ```python
   import numbers

   class IntegerValidator:
       def __init__(self, minimum=None, maximum=None):
            pass
       def __set_name__(self, owner, name):
           pass 
       def __set__(self, instance, value):
            pass

       def __get__(self, instance, owner):
           pass 

   ```

3. **Unit Tests (`testsV1.py`):**
   ```python
   import unittest
   from validatorsV1 import IntegerValidator 

   class TestIntegerValidator(unittest.TestCase):
       def test_valid_integer(self):
           pass

       def test_minimum(self):
            pass
       def test_maximum(self):
            pass

       def test_invalid_type(self):
            pass 
   ```

4. **`CharValidator` Class (Similar to `IntegerValidator`):**
   ```python
   class CharValidator:
       # ... (Implementation analogous to IntegerValidator)
   ```

5. **Unit Tests for `CharValidator` (Similar to `TestIntegerValidator`)**

## Areas for Improvement

- **Test Data Factory:** Create a helper function to streamline test object creation:
   ```python
   @staticmethod
   def create_person(minimum, maximum):
       return type('TestClass', (), {'age': IntegerValidator(minimum=minimum, maximum=maximum)})() 
   ```
   This dynamically creates a `TestClass` with an `age` attribute managed by `IntegerValidator`.

