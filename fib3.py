#Memoization To the rescue

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]






def drive():
    num: int = eval(input("nth fibonacci term: "))
    print(fib3(num))

if __name__ == "__main__":
    drive()
    # print(fib3(10))


