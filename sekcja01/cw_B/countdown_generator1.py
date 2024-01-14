def countdown(n):
    """
    Funkcja generatora odliczająca w dół do wartości 1

    :param n: początkowa wartość
    :return: obiekt generatora
    """
    while n > 0:
        yield n
        n -= 1


if __name__ == '__main__':

    generator = countdown(3)
    print('Utworzono generator countdown(3)')

    nr = 0
    try:
        while True:
            nr += 1
            print(f'\twywołanie #{nr} funkcji next:', next(generator))
    except StopIteration:
        print(f'\twywołanie #{nr} funkcji next: wyjątek StopIteration\n')

    generator = countdown(10)
    print('Utworzono generator countdown(10)')
    print('\twartości z generatora:', *generator)
