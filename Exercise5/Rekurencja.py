def factorial(n):
    if n < 0:
        return "value is smaller than 0"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def fibonacci(n):
    bigger, smaller = 0, 1
    for i in range(1, n+1):
        temp = bigger
        bigger += smaller
        smaller = temp
    return bigger


