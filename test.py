def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = 7
    fib_series = fibonacci(n)
    print(f"The first {n} numbers in the Fibonacci series are: {fib_series}")
