from utils.przyklady import execute
import sys

commands = [
    'sys.byteorder',
    'sys.float_info.max',
    'sys.float_info.max_exp',
    'sys.float_info.max_10_exp',
    'sys.float_info.min',
    'sys.float_info.min_exp',
    'sys.float_info.min_10_exp',
    'sys.float_info.dig',
    'sys.float_info.mant_dig',
    'sys.float_info.epsilon',
    'sys.float_info.radix',
    'sys.float_info.rounds',
    'sys.maxsize',
    'sys.maxunicode',
    'sys.platform',
    'sys.version'
]
execute(commands, globals(), 'Wybrane stałe modułu sys')

commands = [
    'sys.getrecursionlimit()'
]
execute(commands, globals(), 'Wybrane funkcje modułu sys')
