from utils.przyklady import execute
import itertools

commands = [
    """iterator = itertools.product('ABC', '12')
list(iterator)""",

    """iterator = itertools.product('ABC', repeat=2)
list(iterator)""",

    """iterator = itertools.permutations('ABC')
list(iterator)""",

    """iterator = itertools.permutations('ABC', 2)
list(iterator)""",

    """iterator = itertools.combinations('ABC', 2)
list(iterator)""",

    """iterator = itertools.combinations_with_replacement('ABC', 2)
list(iterator)"""
]

execute(commands, globals(), 'Iteratory kombinatoryczne')
