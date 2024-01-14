import timeit
import math


def utworz_liste_pierwiastkow():
    lista = []
    for liczba in range(1_000):
        lista.append(math.sqrt(liczba))
    return lista


czas = timeit.timeit(stmt=utworz_liste_pierwiastkow, number=10_000, globals=globals())
print(f'Czas wykonania: {czas:.3f} s')
