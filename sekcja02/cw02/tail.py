"""
Implementacja polecenia tail.
Składnia polecenia:
   tail /sciezka/do/pliku
   tail -n <liczba_wierszy> /sciezka/do/pliku
   tail --lines <liczba_wierszy> /sciezka/do/pliku
"""
from collections import deque
import sys


def tail(nazwa_pliku, liczba_wierszy):
    """
    Funkcja wypisuje podaną liczbę ostatnich linii z pliku.

    :param nazwa_pliku: sciezka do pliku
    :param liczba_wierszy: liczba ostatnich linii do wypisania
    :return: None
    """
    try:
        with open(nazwa_pliku, mode='rt', encoding='utf-8') as plik:
            koncowe_wiersze = deque(plik, liczba_wierszy)
        for nr, wiersz in enumerate(koncowe_wiersze, start=1):
            print(f'{nr:3}: {wiersz}', end='')
    except OSError as blad:
        print(f'Otwarcie pliku \'{nazwa_pliku}\' zakończyło się błędem: {blad}')


if __name__ == '__main__':

    opcje_polecenia = '-n', '--lines'
    try:
        liczba_ostatnich_wierszy = int(sys.argv[2]) if sys.argv[1] in opcje_polecenia else 10
        nazwa_pliku_do_odczytu = sys.argv[-1]
        tail(nazwa_pliku_do_odczytu, liczba_ostatnich_wierszy)
    except IndexError:
        print('Nieprawidłowa składnia polecenia - błędna liczba argumentów')

