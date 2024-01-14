from utils.przyklady import execute
import itertools

commands = [
    """iterator = itertools.accumulate((1, 2, 3, 4, 5))
list(iterator)""",

    """iterator = itertools.accumulate((1, 2, 3, 4, 5), lambda x, y: x * y)
list(iterator)""",

    """iterator = itertools.batched(range(1, 13), 3)
list(iterator)""",

    """iterator = itertools.chain('ABC', (1, 2), 'XYZ')
list(iterator)""",

    """iterator = itertools.chain.from_iterable(['ABC', (1,2), ['X', 'Y', 'Z']])
list(iterator)""",

    """iterator = itertools.compress('ABCD', [True, False, 1, 0])
list(iterator)""",

    """iterator = itertools.dropwhile(lambda x: len(x) != 4, ['jeden', 'dwa', 'trzy', 'cztery', 'pięć'])
list(iterator)""",

    """iterator = itertools.takewhile(lambda x: len(x) != 4, ['jeden', 'dwa', 'trzy', 'cztery', 'pięć'])
list(iterator)""",

    """iterator = itertools.filterfalse(lambda x: len(x) != 4, ['jeden', 'dwa', 'trzy', 'cztery', 'pięć'])
list(iterator)""",

    """imiona = 'Ania', 'Basia', 'Ala', 'Beata', 'Agata'
{inicjal: list(grupa) for inicjal, grupa in itertools.groupby(sorted(imiona), lambda imie: imie[0])}""",

    """iterator = itertools.islice('ABCDEF', 2, 4)
list(iterator)""",

    """iterator = itertools.pairwise('ABCDEF')
list(iterator)""",

    """iterator = itertools.starmap(lambda x, y: x + y, [(1, 3), (2, 7), (-1, 4)])
list(iterator)""",

    """it1, it2 = itertools.tee([1, 2, 3], 2)
list(it1) + ['*'] + list(it1) + ['*'] + list(it2)""",

    """iterator = itertools.zip_longest('ABCD', '12', fillvalue='?')
list(iterator)"""
]

execute(commands, globals(), 'Iteratory kończące działania wraz z krótszą sekwencją')
