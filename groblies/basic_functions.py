def factorial(n: int) -> int:
    if n == 2:
        return 2
    return n * factorial(n - 1)

def permutation(n: int, choices: int) -> int:
    return factorial(n) / factorial(n - choices)

def combintation(n: int, choices: int) -> int:
    return factorial(n) / (factorial(n - choices) * factorial(choices))
