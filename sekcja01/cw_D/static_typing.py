def get_firstname(fullname: str) -> str:
    return fullname.split()[0]


def greeting(fullname: str) -> None:
    fallback_name: dict[str, str] = {
        'firstname': 'Nieznajomy',
        'lastname': 'Nieznajomy'
    }
    firstname: str = get_firstname(fullname or fallback_name)
    print(f'Witaj {firstname}!')


if __name__ == '__main__':
    greeting('Jan Kowalski')
    greeting('')

# Do analizy statycznej kodu można użyć np. modułu pyright lub mypy

# Z okna terminala:
# - zainstaluj pyright: pip install pyright
# - uruchom analizę:    pyright ./sekcja01/cw_D/static_typing.py
