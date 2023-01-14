from utils.przyklady import execute

commands = [
'''from itertools import count
iterator = count(3)
result = [next(iterator) for _ in range(5)]''',

'''from itertools import cycle
iterator = cycle('abcd')
result = [next(iterator) for _ in range(10)]''',

'''from itertools import repeat
iterator = repeat('A', 7)
result = list(iterator)''']

execute(commands, globals(), 'Iteratory nieskończone')
