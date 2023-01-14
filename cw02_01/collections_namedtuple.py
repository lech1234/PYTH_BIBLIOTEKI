from collections import namedtuple
from pympler.asizeof import asizeof


def to_namedtuple(type_name, dictionary):
    key_names = ' '.join([key for key in dictionary.keys()])
    NamedTuple = namedtuple(type_name, key_names)
    return NamedTuple._make(dictionary.values())


def get_size(name, instance):
    size = asizeof(instance)
    print(f'{name}: {instance}\nsize: {size} bytes')
    return size


if __name__ == '__main__':
    contact_dict = {
        'firstname': 'Jan',
        'lastname': 'Kowalski',
        'phone': '123456789'
    }

    contact_nt = to_namedtuple('Contact', contact_dict)

    dict_size = get_size('DICTIONARY', contact_dict)
    namedtuple_size = get_size('NAMED TUPLE', contact_nt)

    gain = (1 - namedtuple_size / dict_size) * 100
    print(f'Size of named tuple is {gain: .1f}% {"smaller" if gain < 100 else "greater"} than size of dictionary')
