def numer_dnia_tygodnia(data_tekstowa: str, separator: str) -> int:
    dzien: int
    miesiac: int
    rok: int
    z: int
    c: int
    dzien, miesiac, rok = map(int, data_tekstowa.split(sep=separator))
    if miesiac < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2
    return (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7


def nazwa_dnia_tygodnia(numer_dnia: int) -> str:
    nazwa_dnia: tuple[str, ...] = ('niedziela', 'poniedziałek', 'wtorek', 'środa',
                                   'czwartek', 'piątek', 'sobota')
    return nazwa_dnia[numer_dnia]


def jaki_to_dzien(data_tekstowa: str, separator: str) -> None:
    numer: int = numer_dnia_tygodnia(data_tekstowa, separator)
    nazwa: str = nazwa_dnia_tygodnia(numer)
    print('Dzień', data_tekstowa, 'to', nazwa)


data: str = input('Podaj datę (dd-mm-rrrr): ')
jaki_to_dzien(data, '-')
