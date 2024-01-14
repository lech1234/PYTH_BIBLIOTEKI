from utils.przyklady import execute
import os

commands = [
    'os.name',
    'os.curdir',
    'os.pardir',
    'os.sep',
    'os.extsep',
    'os.pathsep'
]

execute(commands, globals(), 'Wybrane stałe modułu os')
