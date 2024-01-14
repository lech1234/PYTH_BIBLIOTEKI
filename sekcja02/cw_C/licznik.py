from utils.przyklady import execute
import collections

commands = [
    "licznik = collections.Counter('abrakadabra')",

    '''iterator = licznik.elements()
list(iterator)''',

    'licznik.most_common(2)',

    '''licznik.subtract('barbara')
licznik''',

    '''licznik.update(a=-4, b=2)
licznik''']

execute(commands, globals(), 'Działanie licznika Counter')