class PodwojnyIterator:
    """
    Klasa implementuje protokół iteratora.
    """

    def __init__(self, start, stop=None):
        """
        Metoda definiuje zakres iteratora.

        :param start: wartość początkowa (inclusive), jeśli podano 2 argumenty
                      w przeciwnym razie (jeśli podano tylko 1 argument - wartość końcowa
        :param stop: wartość końcowa (inclusive), jeśli podano 2 argumenty
                     w przeciwnym razie - None.

        Metoda tworzy atrybuty instancyjne:
        __stop  - wartość końcowa iteratora
        __biezaca_wartosc - wartość aktualnie zwracana
        __czy_zwiekszac - wartość logiczna określająca, czy bieżącą wartość należy zinkrementować,
                          czy powtórzyć
        """
        self.__biezaca_wartosc, self.__stop = (-1, start) if stop is None else (start - 1, stop)
        self.__czy_zwiekszac = True  # czy zwiększyć licznik, czy też powtórzyć tę samą wartość drugi raz?

    def __iter__(self):
        """
        Metoda protokołu iteratora.

        :return: instancja iteratora
        """
        return self

    # metoda iteratora - zwraca kolejną wartość
    def __next__(self):
        """
        Metoda protokołu iteratora.

        :return: kolejna wartość lub powtórzenie bieżącej
        """
        if self.__biezaca_wartosc < self.__stop:
            if self.__czy_zwiekszac:
                self.__biezaca_wartosc += 1
            self.__czy_zwiekszac = not self.__czy_zwiekszac
            return self.__biezaca_wartosc
        else:
            if not self.__czy_zwiekszac:
                self.__czy_zwiekszac = True
                return self.__biezaca_wartosc
            raise StopIteration


if __name__ == '__main__':
    iterator = PodwojnyIterator(4)
    print('Wartości z iteratora (zakres 0..4): ', end='')
    print(*iterator, sep=', ')

    print('Wartości z iteratora (zakres 2..4): ', end='')
    iterator = PodwojnyIterator(2, 4)
    print(*iterator, sep=', ')
