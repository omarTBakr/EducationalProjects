import unittest
# from validatorV1 import IntegerValidator , CharValidator
from vlidatorV2 import IntegerValidator
from vlidatorV2 import CharacterValidator as CharValidator

class TestIntegerValidator(unittest.TestCase):

    def test_minimum(self):
        """
        Test setting a value below the minimum
        """

        class Person:
            age = IntegerValidator(minimum=1)

        person = Person()
        with self.assertRaises(ValueError) :
            person.age = 0

    def test_maximum(self):
        """
            Test setting a value greater than  the minimum
            """
        class Person:
            age = IntegerValidator(maximum=10)

        person = Person()
        with self.assertRaises(ValueError):
            person.age = 12


    def test_range(self):
        """
        Test setting a correct value in the range
        """
        class Person:
            age = IntegerValidator(minimum=1, maximum= 100)

        person = Person()

        person.age = 23

    def test_get(self):
        """
            Test instance.__get__()
        """
        class Person:
            age = IntegerValidator(minimum=1)

        person = Person()

        person.age = 100

        self.assertEqual(100 , person.age)

    def test_get2(self):
        """
        Test Person.age
        """
        class Person:
            age = IntegerValidator(minimum=1)

        obj = Person()

        self.assertIsInstance(type(obj).age , IntegerValidator)




class TestCharValidator(unittest.TestCase):

    def test_minimum(self):
        class Person:
            name = CharValidator(minimum=1)

        person = Person()
        with self.assertRaises(ValueError):
            person.name = ''


    def test_maximum(self):
        class Person:
            name = CharValidator(maximum=10)

        person = Person()
        with self.assertRaises(ValueError):
            person.name = '12345678901112'


    def test_range(self):
        class Person:
            name= CharValidator(minimum=1, maximum= 100)

        person = Person()

        person.name = 'omar'

    def test_get(self):
        class Person:
            name= CharValidator(minimum=1)

        person = Person()
        name = 'omar'
        person.name = name

        self.assertEqual(name , person.name)