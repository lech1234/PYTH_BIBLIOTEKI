def double_generator(start, stop=None):
    if stop is None:
        stop = start
        start = 0
    current = start - 1
    while current < stop:
        current += 1
        yield current
        yield current


if __name__ == '__main__':
    double_gen = double_generator(3)
    print(list(double_gen))
    double_gen = double_generator(1, 3)
    print(list(double_gen))
