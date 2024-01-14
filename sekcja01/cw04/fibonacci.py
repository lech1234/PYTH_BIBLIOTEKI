from functools import lru_cache
import time


def fib_bez_cache(n):
    """
    Funkcja oblicza wyrazy ciągu Fibonacciego bez cache'owania wyników.

    :param n: numer wyrazu ciągu Fibonacciego (numeracja od 1)
    :return: wartość wyrazu ciągu Fibonacciego
    """
    if n < 3:
        return 1
    return fib_bez_cache(n - 1) + fib_bez_cache(n - 2)


@lru_cache(maxsize=3)
def fib_z_cache(n):
    """
    Funkcja oblicza wyrazy ciągu Fibonacciego cache'ując wyniki.

    :param n: numer wyrazu ciągu Fibonacciego (numeracja od 1)
    :return: wartość wyrazu ciągu Fibonacciego
    """
    if n < 3:
        return 1
    return fib_z_cache(n - 1) + fib_z_cache(n - 2)


if __name__ == '__main__':
    def zmierz_czas_wykonania(funkcja, *args, **kwds):
        """
        Funkcja mierzy i wypisuje czas wykonania podanej funkcji oraz jej wynik

        :param funkcja: funkcja, której mierzymy czas wykonania.
        :param args: krotka argumentów pozycyjnych funkcji
        :param kwds: słownik argumentów nazwanych funkcji
        :return: None
        """
        start = time.time()  # Czas rozpoczęcia pomiaru
        wynik = funkcja(*args, **kwds)
        stop = time.time()  # Czas zakończenia pomiaru
        argument = args[0] if args else kwds['n']
        print(f'F[{argument}] = {wynik}, Czas wykonania: {stop - start:.3f} s (funkcja: {funkcja.__name__})')


    nr_wyrazu_ciagu = 38
    zmierz_czas_wykonania(fib_bez_cache, nr_wyrazu_ciagu)
    zmierz_czas_wykonania(fib_z_cache, nr_wyrazu_ciagu)
    print(fib_z_cache.cache_info())
