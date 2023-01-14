import timeit
from functools import lru_cache


# funkcja oblicza wyrazy ciągu Fibonacciego bez cache'owania wyników
def fib_without_cache(n):
    if n < 3:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


# funkcja oblicza wyrazy ciągu Fibonacciego cache'ując wyniki
@lru_cache(maxsize=3)
def fib_with_cache(n):
    if n < 3:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)


# funkcja mierzy i wypisuje czas wykonania podanej funkcji oraz jej wynik
def measure_execution_time(function, *args):
    result = None

    # czas wykonania tej funkcji będzie mierzony
    # funkcja jest bezargumentowa
    def function_to_execute():
        nonlocal result  # ta deklaracja umożliwia zmianę wartości zmiennej na zewnątrz funkcji
        result = function(*args)

    execution_time = timeit.timeit(stmt=function_to_execute, number=1, globals=globals())
    print(f'Result: {result}')
    print(f'Execution time: {execution_time:.3f} s (function: {function.__name__})')


if __name__ == '__main__':
    measure_execution_time(fib_without_cache, 35)
    measure_execution_time(fib_with_cache, 35)
