def get_firstname(fullname):
    return fullname.split()[0]


def greeting(fullname):
    fallback_name = {
        'firstname': 'Nieznajomy',
        'lastname': 'Nieznajomy'
    }
    firstname = get_firstname(fullname or fallback_name)
    print(f'Witaj {firstname}!')


if __name__ == '__main__':
    greeting('Jan Kowalski')
    greeting('')
