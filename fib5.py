#Keep it Simple Fibonacci
#iterative Solution

def fib5(n: int) -> int:
    if n == 0: return #special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next # Tuple unpacking
    return next

if __name__ == "__main__":
    print(fib5(6))
    print(fib5(70))


