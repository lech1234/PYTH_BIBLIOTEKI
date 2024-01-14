import timeit

init = 'import math'

kod = '''
def utworz_liste_pierwiastkow():
    lista = []
    for liczba in range(1_000):
        lista.append(math.sqrt(liczba))
    return lista

utworz_liste_pierwiastkow()
'''

timer = timeit.Timer(setup=init, stmt=kod)
czas = timer.timeit(number=10_000)
print(f'Czas wykonania: {czas:.3f} s')

# można też tak:
czas = timeit.timeit(setup=init, stmt=kod, number=10_000)
print(f'Czas wykonania: {czas:.3f} s')
