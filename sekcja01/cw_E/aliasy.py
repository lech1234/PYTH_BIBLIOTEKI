from typing import Iterable

type U = int | float | complex  # alias
type Wektor = Iterable[U]  # alias


def iloczyn_skalarny(v1: Wektor, v2: Wektor) -> U:
    return sum(x * y for x in v1 for y in v2)


if __name__ == '__main__':
    print(iloczyn_skalarny((1, 2, 3), [4, 5, 6]))
    print(iloczyn_skalarny((1, 2, 3), [4.0, 5.0, 6.0]))
    print(iloczyn_skalarny((1.0, 2.0, 3.0), [4.0, 5.0, 6.0]))
