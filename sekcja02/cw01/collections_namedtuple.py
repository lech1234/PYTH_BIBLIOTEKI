"""
Moduł porównuje wielkość słownika i krotki nazwanej zawierającej te same dane.
"""
from collections import namedtuple
import pympler.asizeof as pmp


def zamien_na_krotke_nazwana(nazwa_typu, slownik):
    """
    Funkcja konwertuje słownik na krotkę nazwaną.

    :param nazwa_typu: nazwa typu krotki nazwanej
    :param slownik: słownik typu dict
    :return: instancja krotki nazwanej
    """
    PodklasaKrotkiNazwanej = namedtuple(nazwa_typu, slownik.keys())
    return PodklasaKrotkiNazwanej._make(slownik.values())


def oblicz_rozmiar(opis, instancja):
    """
    Funkcja zwraca rozmiar podanego obiektu.

    :param opis: opis typu instancji
    :param instancja: instancja
    :return: rozmiar instancji
    """
    rozmiar_instancji = pmp.asizeof(instancja)
    print(f'{opis} ({instancja.__class__.__name__}):')
    print(f'\tinstancja: {instancja}')
    print(f'\trozmiar:   {rozmiar_instancji} B\n')
    return rozmiar_instancji


if __name__ == '__main__':
    
    kontakt_dict = {
        'imie': 'Jan',
        'nazwisko': 'Kowalski',
        'telefon': '123456789'
    }
    rozmiar_slownika = oblicz_rozmiar('SŁOWNIK', kontakt_dict)

    kontakt_namedtuple = zamien_na_krotke_nazwana('Kontakt', kontakt_dict)
    rozmiar_krotki = oblicz_rozmiar('KROTKA NAZWANA', kontakt_namedtuple)

    zysk_w_procentach = (1 - rozmiar_krotki / rozmiar_slownika) * 100
    print(f'Rozmiar krotki nazwanej jest o {zysk_w_procentach:.1f}% '
          f'{"mniejszy" if zysk_w_procentach < 100 else "większy"} niż rozmiar słownika')
