class LetterIterator:
    """
    Klasa iteratora zwracającego n kolejnych liter począwszy od A
    """
    def __init__(self, n=26):
        if n < 0:
            n = 0
        if n > 26:
            n = 26
        self.__current_letter_code = ord('A') - 1
        self.__last_letter_code = ord('A') + n

    # protokół iteracji
    def __iter__(self):
        return self

    def __next__(self):
        self.__current_letter_code += 1
        if self.__current_letter_code < self.__last_letter_code:
            return chr(self.__current_letter_code)
        else:
            raise StopIteration()


if __name__ == '__main__':

    iterator = LetterIterator(3)
    print('Utworzono LetterIterator(3)')
    nr = 0
    try:
        while True:
            nr += 1
            print(f'\twywołanie #{nr} funkcji next:', next(iterator))
    except StopIteration:
        print(f'\twywołanie #{nr} funkcji next: wyjątek StopIteration\n')

    iterator = LetterIterator(10)
    print('Utworzono LetterIterator(10)')
    print('\twartości z iteratora:', *iterator)
