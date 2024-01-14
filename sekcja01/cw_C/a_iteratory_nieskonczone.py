from utils.przyklady import execute
import itertools

commands = [
    '''iterator = itertools.count(3)
[next(iterator) for _ in range(7)]''',

    '''iterator = itertools.cycle(('tak', 'nie'))
[next(iterator) for _ in range(7)]''',

    '''iterator = itertools.repeat('*')
[next(iterator) for _ in range(7)]''',

    '''iterator = itertools.repeat('A', 7)
list(iterator)''']

execute(commands, globals(), 'Iteratory nieskończone')
