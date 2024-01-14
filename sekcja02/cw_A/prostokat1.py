from collections import namedtuple

Prostokat = namedtuple('Prostokat', ['szerokosc', 'wysokosc'], defaults=[1])

prostokat1 = Prostokat(4, 7)
# użycie indeksów
pole_prostokata = prostokat1[0] * prostokat1[1]

# użycie nazw pól
obwod_prostokata = 2 * (prostokat1.szerokosc + prostokat1.wysokosc)
a, b = prostokat1
print('Szerokość prostokąta:', a)
print('Wysokość prostokąta:', b)

print('Nazwy pól:', prostokat1._fields)
print('Wartości domyślne:', prostokat1._field_defaults)
