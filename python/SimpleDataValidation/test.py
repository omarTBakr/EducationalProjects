from main import SchemaValueError, SchmaError, SchemaKeyError
from main import validate_types, validate_keys


def test_validate_keys():
    template  = { 'first': int , 'second': str  ,
                  'third':dict
                  }
    test1 = { 'first': 23 , 'second': 'test1'  ,
                  'third': { }
                  }
    test2 = { 'first': int , 'second': str  ,

                  }
    test3= {'first': int, 'second': str,
            'forth':int
             }

    for test in [test1 , test2 , test3]:
        try:
            validate_keys(template , test, '')

        except SchmaError as error:
            print('\nValidation error\n', error)


def test_validate_types():
    template = {'first': int, 'second': str,
                'third': dict
                }
    test1 = {'first': 23, 'second': 'test1',
             'third': {}
             }
    test2 = {'first': 'int', 'second': 23,

             }
    test3 = {'first': 'int', 'second': 'str',
             'forth': 'forth'
             }

    for test in [test1, test2, test3]:
        try:
            validate_types(template, test, '')

        except SchmaError as error:
            print('\nValidation error\n', error)


if __name__=='__main__':

    # print( validate_keys(eric , template,''))
    test_validate_keys()