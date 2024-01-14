from collections import namedtuple

Prostokat = namedtuple('Prostokat', 'szerokosc, wysokosc')

wymiary = [3, 5]
prostokat1 = Prostokat._make(wymiary)
print('Prostokąt #1:', prostokat1)

slownik = prostokat1._asdict()
print('Słownik:', slownik)

prostokat2 = prostokat1._replace(wysokosc=2)
print('Prostokąt #2:', prostokat2)
