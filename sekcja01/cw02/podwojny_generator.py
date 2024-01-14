def podwojny_generator(start, stop=None):
    """
    Implementacja generatora.

    :param start: wartość początkowa (incl.), jeśli podano 2 argumenty
                  w przeciwnym razie (jeśli podano tylko 1 argument) - wartość końcowa
    :param stop: wartość końcowa (incl.), jeśli podano 2 argumenty
                 w przeciwnym razie - None.
    :return: generator
    """
    if stop is None:
        start, stop = 0, start
    biezaca_wartosc = start - 1
    while biezaca_wartosc < stop:
        biezaca_wartosc += 1
        yield biezaca_wartosc
        yield biezaca_wartosc


if __name__ == '__main__':
    generator = podwojny_generator(4)
    print('Wartości z generatora (zakres 0..4): ', end='')
    print(*generator, sep=', ')

    print('Wartości z generatora (zakres 2..4): ', end='')
    generator = podwojny_generator(2, 4)
    print(*generator, sep=', ')
