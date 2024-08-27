"""
this module will contain the implementation of Mod class Only
"""

import numbers
import functools
import operator


@functools.total_ordering
class Mod:
    def __init__(self, modulus, value):
        # check that both are int
        Mod.validate_number(modulus, 0)
        Mod.validate_number(value, value)
        self._modulus = modulus

        self._value = value % self._modulus

    @staticmethod
    def validate_number(number, lower_limit):
        if not (isinstance(number, numbers.Integral) and number >= lower_limit):
            raise ValueError(f'number must be real and > {lower_limit}')

    @property
    def modulus(self):
        return self._modulus

    @property
    def value(self):
        return self._value

    @staticmethod
    def is_same_modulus(other, mod):
        if other.modulus != mod:
            raise TypeError('modulus must be the same')

    def __eq__(self, other):
        """
        two  Mod is said to be equal if they are a congruent
        :param other: int or Mod object
        :return:  True if their residue is equal
        """

        if isinstance(other, int):
            other = Mod(self.modulus, other)

        elif isinstance(other, Mod):
            Mod.is_same_modulus(other, self.modulus)
        else:
            raise TypeError('un supported operand')

        return bool(abs(self.value - other.value) % self.modulus == 0)

    def __hash__(self):
        return hash((self.modulus, self.value))

    def __int__(self):
        return self.value

    def __repr__(self):
        return f'Mod(modulus={self.modulus} , value={self.value})'

    def do_operation(self, other, op, inplace=False):
        if isinstance(other, int):
            other = Mod(self.modulus, other % self.modulus)
        elif isinstance(other, Mod):
            Mod.is_same_modulus(other, self.modulus)
        else:
            raise TypeError(f'un supported {op.__name__} between Mod and {type(other)}')
        result = op(self.value, other.value)
        if inplace:
            self._value = result
            return self
        return Mod(self.modulus, result)

    def __add__(self, other):
        self.do_operation(other, operator.add)

    def __iadd__(self, other):
        self.do_operation(other, operator.add, inplace=True)

    def __sub__(self, other):
        self.do_operation(other, operator.sub)

    def __isub__(self, other):
        self.do_operation(other, operator.sub, inplace=True)

    def __mul__(self, other):
        self.do_operation(other, operator.mul)

    def __imul__(self, other):
        self.do_operation(other, operator.mul, inplace=True)

    def __pow__(self, other):
        self.do_operation(other, operator.pow)

    def __ipow__(self, other):
        self.do_operation(other, operator.pow, inplace=True)

    def __lt__(self, other):
        if isinstance(other, Mod):
            Mod.is_same_modulus(other, self.modulus)
            return self.value < other.value

        if isinstance(other, int):
            return self.value < other % self.modulus

        raise TypeError(f'un supported comparison between Mod  and {type(other)}')
