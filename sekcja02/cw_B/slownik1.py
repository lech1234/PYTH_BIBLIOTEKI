from collections import defaultdict

slownik = defaultdict(lambda: 'wartość domyślna')
slownik['a'] = 1
slownik['b'] = 2
print('zawartość słownika:', slownik)

print("slownik['a'] =", slownik['a'])
print("slownik['b'] =", slownik['b'])
print("slownik['c'] =", slownik['c'])

print('zawartość słownika:', slownik)
