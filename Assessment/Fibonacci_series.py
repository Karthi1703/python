def fibonacci_recursive(n: int) -> list:
    def fib(a, b, n):
        while n<0:
            return []
        else:
            return [a] + fib(b, a + b, n - 1)

    return fib(0, 1, n)

print(fibonacci_recursive(10))