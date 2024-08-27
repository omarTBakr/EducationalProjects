# Simple Modulus Class

This project enhances your implementation skills. It's fairly straightforward to implement. Here are the requirements:

1. Make a `Mod` class that supports the following:
   1. Has instance variables `module` and `residue`.
   2. Make `module` and `residue` read-only properties.
   3. Implement `__eq__` between an `int` and a `Mod`, or two `Mod` objects. They must be equal if and only if they are congruent [for more info](https://en.wikipedia.org/wiki/Modular_arithmetic).
   4. Implement `__hash__`.
   5. Implement `__int__`.
   6. Implement `__repr__`.
   7. Implement `__add__` and `__iadd__`.
   8. Implement `__sub__` and `__isub__`.
   9. Implement `__mul__` and `__imul__`.
   10. Implement `__pow__` and `__ipow__`.
   11. Implement comparison operators.

2. Write proper tests for each functionality (I myself am guilty of not doing proper testing :-)).

## Areas for Improvement

1. More proper testing for total ordering.
2. Code could use some restructuring.
