def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


num = int(input('Enter a number: '))
print(f'Factorial of {num} is: {factorial(num)}')