from utils.przyklady import execute

commands = [
"""from itertools import product
iterator = product('ABC', '12')
result = list(iterator)""",

"""from itertools import product
iterator = product('ABC', repeat=2)
result = list(iterator)""",

"""from itertools import permutations
iterator = permutations('ABC')
result = list(iterator)""",

"""from itertools import permutations
iterator = permutations('ABC', 2)
result = list(iterator)""",

"""from itertools import combinations
iterator = combinations('ABC', 2)
result = list(iterator)""",

"""from itertools import combinations_with_replacement
iterator = combinations_with_replacement('ABC', 2)
result = list(iterator)"""
]
execute(commands, globals(), 'Iteratory kombinatoryczne')
