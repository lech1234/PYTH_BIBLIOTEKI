from collections import deque
import sys


# syntax:
#   tail /path/to/file
#   tail -n <number_of_lines> /path/to/file
#   tail --lines <number_of_lines> /path/to/file

def tail(file_name, number_of_lines):
    try:
        with open(file_name, mode='rt', encoding='utf-8') as file:
            end_lines = deque(file, number_of_lines)
        for nr, line in enumerate(end_lines, start=1):
            print(f'{nr:3}: {line}', end='')
    except OSError as error:
        print(f'Opening file "{file_name}" failed with error: {error}')


if __name__ == '__main__':
    tail_options = '-n', '--lines'
    lines = int(sys.argv[2]) if sys.argv[1] in tail_options else 10
    filename = sys.argv[-1]
    tail(filename, lines)
