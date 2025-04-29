'Factorial'
n = int(input('Enter a number: '))
def factorial(n: int) -> int:
    'Return the factorial of n'
    if n < 0:
        raise ValueError('n must be >= 0')
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(f'The factorial of {n} is {factorial(n)}')