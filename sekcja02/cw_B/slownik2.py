from collections import defaultdict
from itertools import starmap

slownik = defaultdict(list)
miesiace = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
            'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')

# wstawienie danych do słownika
for miesiac in miesiace:
    slownik[len(miesiac)].append(miesiac)

najdluzsza_nazwa = max(map(len, miesiace))

for dlugosc in range(1, najdluzsza_nazwa + 1):  # zakres długości nazw miesięcy
    print(f'{dlugosc:2}: {slownik[dlugosc]}')
