class DoubleIterator:
    def __init__(self, start, stop=None):
        # ustawienie wartości początkowej i końcowej licznika (obie wartości inclusive)
        if stop is None:
            self.__start = 0
            self.__stop = start
        else:
            self.__start = start
            self.__stop = stop
        self.__current = self.__start - 1  # bieżąca wartość licznika
        self.__increment = True  # czy zwiększyć licznik, czy też powtórzyć tę samą wartość drugi raz?

    def __iter__(self):
        return self  # zwrócenie obiektu iteratora

    # metoda iteratora - zwraca kolejną wartość
    def __next__(self):
        if self.__current < self.__stop:
            if self.__increment:
                self.__current += 1
            self.__increment = not self.__increment
            return self.__current
        else:
            if not self.__increment:
                self.__increment = True
                return self.__current
            raise StopIteration


if __name__ == '__main__':
    double_iter = DoubleIterator(3)
    print(list(double_iter))
    double_iter = DoubleIterator(1, 3)
    print(list(double_iter))
