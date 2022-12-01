# a direct mechanical translation of the formula
# fib(n) = fib(n - 1) + fib(n - 2)

# throws a RecursionError: maximum recusion depth reached
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(5))
