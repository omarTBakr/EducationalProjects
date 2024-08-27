from Mod import Mod
import unittest


class TestMod(unittest.TestCase):
    def test_float_initialization(self):
        value, mod = 1.1, 2.2
        self.assertRaises(ValueError, Mod, mod, value)

    def test_negative_mod(self):
        value, mod = 1, -2
        self.assertRaises(ValueError, Mod, mod, value)

    def test_correct_initialization(self):
        mod, value, residue = 3, 15, 0
        mod = Mod(mod, value)
        self.assertEqual(mod.value, residue)

    def test_equality(self):
        test_obj = Mod(3, 30)

        # both are congruent so they pass
        self.assertEqual(test_obj, Mod(3, 15))

        # Mod with int, compare the residue so they pass
        self.assertEqual(test_obj, 0)

        # compare with float thus raising TypeError
        self.assertRaises(TypeError, test_obj.__eq__, 12.2)

        # compare with str, raise TypeError
        self.assertRaises(TypeError, test_obj.__eq__, '12.2')

        # comapre Mod with another Mod but with different Modulus raises TypeError.
        self.assertRaises(TypeError, Mod(4, 15).__eq__, test_obj)
