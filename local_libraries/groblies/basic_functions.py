__all__ = [
"factorial",
"permutation",
"combination"
]

def factorial(n: int) -> int:
    if n == 2:
        return 2
    return n * factorial(n - 1)

def permutation(n: int, choices: int) -> int:
    return factorial(n) / factorial(n - choices)

def combination(n: int, choices: int) -> int:
    return factorial(n) / (factorial(n - choices) * factorial(choices))
