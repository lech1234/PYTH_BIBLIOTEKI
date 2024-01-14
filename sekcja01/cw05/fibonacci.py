from sekcja01.cw04.fibonacci import fib_z_cache, fib_bez_cache
import timeit


def zmierz_czas_wykonania(funkcja, *args, **kwds):
    """
    Funkcja dokonuje pomiaru czasu podanej funkcji i wypisuje wynik.

    :param funkcja: funkcja, której mierzymy czas wykonania
    :param args: argumenty funkcji
    :return: None
    """
    wynik = None  # zmienna docelowo otrzyma wartość zwróconą przez funkcję, której czas mierzymy

    def funkcja_do_wywolania():
        """
        Bezargumentowa funkcja wrappera przekazywana jako argument do funkcji timeit.

        :return: None
        """
        nonlocal wynik  # ta deklaracja umożliwia zmianę wartości zmiennej znajdującej się na zewnątrz funkcji
        wynik = funkcja(*args, **kwds)

    czas_wykonania = timeit.timeit(stmt=funkcja_do_wywolania, number=1, globals=globals())
    argument = args[0] if args else kwds['n']
    print(f'F[{argument}] = {wynik}, Czas wykonania: {czas_wykonania:.3f} s (funkcja: {funkcja.__name__})')


if __name__ == '__main__':
    nr_wyrazu_ciagu = 38

    zmierz_czas_wykonania(fib_bez_cache, nr_wyrazu_ciagu)
    zmierz_czas_wykonania(fib_z_cache, nr_wyrazu_ciagu)
