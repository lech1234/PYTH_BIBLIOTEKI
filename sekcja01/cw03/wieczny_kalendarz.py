"""
Moduł definiuje funkcje służące określeniu nazwy dnia tygodnia na podstawie podanej daty.
"""


def __numer_dnia_tygodnia(data: str, separator: str) -> int:
    """
    Funkcja konwertuje datę na numer dnia tygodnia.

    :param data: data w postaci tekstu, w kolejności: dzień, miesiąc, rok
    :param separator: separator oddzielający dzień od miesiąca i miesiąc od roku
    :return: numer dnia tygodnia (0 - niedziela, 1 - poniedziałek, ..., 6 - sobota)
    """
    dzien: int
    miesiac: int
    rok: int
    z: int
    c: int
    dzien, miesiac, rok = map(int, data.split(sep=separator))

    if miesiac < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2
    return (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7


def __nazwa_dnia_tygodnia(numer_dnia: int) -> str:
    """
    Funkcja konwertuje numer dnia tygodnia na jego nazwę.

    :param numer_dnia: numer dnia tygodnia (0, 1, ..., 6)
    :return: nazwa dnia tygodnia
    """
    nazwa_dnia: tuple[str, ...] = ('niedziela', 'poniedziałek', 'wtorek',
                                   'środa', 'czwartek', 'piątek', 'sobota')
    return nazwa_dnia[numer_dnia]


def jaki_to_dzien(data: str, *, sep: str = '-') -> None:
    """
    Funkcja wypisuje podaną datę i nazwę dnia tygodnia odpowiadającą tej dacie.

    :param data: data w postaci tekstu, w kolejności: dzień, miesiąc, rok
    :param sep: separator oddzielający dzień od miesiąca i miesiąc od roku
    :return: None
    """
    numer: int = __numer_dnia_tygodnia(data, sep)
    nazwa: str = __nazwa_dnia_tygodnia(numer)
    print(f'W dniu {data} wypada {nazwa}')


if __name__ == '__main__':
    jaki_to_dzien('24/12/2023', sep='/')
    jaki_to_dzien('25-12-2023', sep='-')
    jaki_to_dzien('26-12-2023')
