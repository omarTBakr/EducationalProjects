from validatorV1 import IntegerValidator, CharValidator
class Person :
    name = CharValidator(maximum= 100)
    age = IntegerValidator(minimum= 0 , maximum=100)

    def __init__(self , name , age):
        self.name =name
        self.age = age

if __name__ == '__main__':
    person = Person('omar', 23)
    print(person.name, person.age)
