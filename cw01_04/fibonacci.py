from functools import lru_cache
import time


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
    start_time = time.time()  # Execution start time
    result = function(*args)
    stop_time = time.time()  # Execution end time
    print(f'Result: {result}')
    print(f'Execution time: {stop_time - start_time:.3f} s (function: {function.__name__})')


if __name__ == '__main__':
    measure_execution_time(fib_without_cache, 35)
    measure_execution_time(fib_with_cache, 35)
    # print(fib_with_cache.cache_info())