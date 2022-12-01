# Automatic memoization
# fib3() can further be simplified

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int: #Same defintion as fib2()
    if n < 2: #base case
        return n
    return fib4(n - 2) + fib4(n - 1)

if __name__ == "__main__":
    print(fib4(6))
    print(fib4(30))
