from typing import Iterable, TypeVar

T = TypeVar('T', int, float, complex)  # typ generyczny
Wektor = Iterable[T]  # alias


def iloczyn_skalarny(v1: Wektor[T], v2: Wektor[T]) -> T:
    return sum(x * y for x in v1 for y in v2)


if __name__ == '__main__':

    print(iloczyn_skalarny((1, 2, 3), [4, 5, 6]))
    print(iloczyn_skalarny((1, 2, 3), [4.0, 5.0, 6.0]))
    print(iloczyn_skalarny((1.0, 2.0, 3.0), [4.0, 5.0, 6.0]))
