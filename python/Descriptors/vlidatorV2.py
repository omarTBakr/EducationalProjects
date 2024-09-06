
import numbers
class BaseValidator:
    def __init__(self, minimum=None, maximum = None):
        self.minimum = minimum
        self.maximum = maximum

    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__.get(self.name , None)



class IntegerValidator(BaseValidator):
    def __set__(self, instance, value):
        if not isinstance(value , numbers.Integral):
            raise ValueError(f'{self.name} must be Integer')

        if self.minimum is not None and value < self.minimum:
            raise ValueError(f'{self.name} must be <{self.minimum}')

        if self.maximum is not None and value > self.maximum:
            raise ValueError(f'{self.name} must be > {self.maximum}')

        instance.__dict__[self.name] = value


class CharacterValidator(BaseValidator):
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.name} must be str')

        if self.minimum and len(value) < self.minimum:
            raise ValueError(f'{self.name} must be <{self.minimum}')

        if self.maximum is not None and len(value) > self.maximum:
            raise ValueError(f'{self.name} must be > {self.maximum}')

        instance.__dict__[self.name] = value