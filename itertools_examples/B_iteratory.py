from utils.przyklady import execute

commands = [
"""from itertools import accumulate
iterator = accumulate((1, 2, 3, 4, 5))
result = list(iterator)""",
"""from itertools import accumulate
iterator = accumulate((1, 2, 3, 4, 5), lambda x, y: x * y)
result = list(iterator)""",

"""from itertools import chain
iterator = chain('ABC', (1,2), 'XYZ')
result = list(iterator)""",

"""from itertools import chain
iterator = chain.from_iterable(['ABC', (1,2), 'XYZ'])
result = list(iterator)""",

"""from itertools import compress
iterator = compress('ABCD', [True, False, 1, 0])
result = list(iterator)""",

"""from itertools import dropwhile
iterator = dropwhile(lambda x: x != 13, range(11, 16))
result = list(iterator)""",

"""from itertools import filterfalse
iterator = filterfalse(lambda x: 3 <= x <= 5, range(10))
result = list(iterator)""",

"""from itertools import islice
iterator = islice('ABCDEF', 2, 4)
result = list(iterator)""",

"""from itertools import pairwise
iterator = pairwise('ABCDEFGH')
result = list(iterator)""",

"""from itertools import starmap
iterator = starmap(lambda x, y: x + y, [(1, 3), (2, 7), (-1, 4)])
result = list(iterator)""",

"""from itertools import takewhile
iterator = takewhile(lambda x: len(x) < 5, ['one', 'two', 'three', 'four'])
result = list(iterator)""",

"""from itertools import zip_longest
iterator = zip_longest('ABCD', '12', fillvalue='?')
result = list(iterator)"""
]
execute(commands, globals(), 'Iteratory kończące działania wraz z krótszą sekwencją')
