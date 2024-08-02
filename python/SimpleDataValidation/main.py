
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}
class SchmaError(Exception):
    pass

class SchemaKeyError(SchmaError,TypeError):
    pass

class SchemaValueError(SchmaError):
    pass

def validate_keys(template,data,path):
    '''
    this function will take the template and a dictionary
    and validate that keys of dictionary matches the ones
    in template
    :param template:
    :param data:
    :param path:
    :return: None
    :raise : SchemaKeyError
    '''
    template_keys = template.keys()
    data_keys = data.keys()

    missing_keys = template_keys - data_keys
    missing_error_message = ','.join( [key for key in missing_keys]
                              )+' is missing ' if missing_keys else ''

    extra_keys = data_keys - template_keys
    extra_error_message = ', '.join([ key for key in extra_keys ]
                              )+ ' is extra'if extra_keys else ' '

    over_all = ' '.join((extra_error_message ,
                         missing_error_message))
    if missing_keys or extra_keys:
        raise SchemaKeyError(over_all)


def validate_types(tempalte, data,path):
    '''
    this function will take a tempalte and a dictionary
    and match the values of that dictionary to the ones
    in the template
    :param tempalte:
    :param data:
    :param path: initial path you want to start from
    :return: None
    :raise SchemaValueError
    '''
    for key, value in tempalte.items():
        if isinstance(value, dict):
            template_type = dict
        else :
            template_type = value

        data_value = data.get(key, None)
        if not isinstance(data_value , template_type):
            error_message = (f'incrrect type {path}'
                             f'-> expected {template_type}'
                             f' found {type(data_value)}')
            raise SchemaValueError(error_message)


def recursive_validate(template, data, path):

    '''
    this function will recursively call itself overy
    any nested dictionaries in data to validate both
    keys and values
    :param template:
    :param data:
    :param path:
    :return: None
    :raise SchemaValueError or SchemaTypeError
    '''
    validate_keys(template,data,path)
    validate_types(template,data,path)

    dictionaries = { key
       for key , value in data.items()
       if isinstance(value , dict)
    }
    for key  in dictionaries:
        sub_path = path + '.' + str(key)
        recursive_validate(template[key],data[key], sub_path)

def validate(template, data):
    '''
    this function is just a thin wrapper around
    recursive_validate
    :param template:
    :param data:
    :return:
    '''
    recursive_validate(template,data,' ')

if __name__ == '__main__':
    validate(template, michael)

