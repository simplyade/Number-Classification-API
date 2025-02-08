

"""
Number Classifier Module

This module provides functions for classifying numbers based on their properties.
"""

def is_prime(number: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    return True

def is_perfect(number: int) -> bool:
    """
    Checks if a number is perfect (i.e., the sum of its proper divisors equals the number).

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

def is_armstrong(number: int) -> bool:
    """
    This ensures to checks if a number is an Armstrong number (i.e., the sum of its digits raised to the power of the number of digits equals the number).

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number

def is_fun_fact(number: int) -> str:
    """
    Generates a fun fact about a number, specifically whether it's an Armstrong number.

    Args:
        number (int): The number for which to generate a fun fact.

    Returns:
        str: A fun fact about the number.
    """
    armstrong_eq = " + ".join([f"{digit}^{len(str(number))}" for digit in str(number)])
    result = is_armstrong(number)
    if result:
        return f"{number} is an Armstrong number because {armstrong_eq} = {number}"
    else:
        return f"{number} is not an Armstrong number"

def classify_number(number: int) -> dict:
    """
    Classifies a number based on its properties.

    Args:
        number (int): The number to classify.

    Returns:
        dict: A dictionary containing the classification results.
    """
    try:
        number = int(number)
    except ValueError:
        return {"number": "alphabet", "error": True}
    is_prime_result = is_prime(number)
    is_perfect_result = is_perfect(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")
    digit_sum = sum(int(digit) for digit in str(number))
    return {
        "number": number,
        "is_prime": is_prime_result,
        "is_perfect": is_perfect_result,
        "properties": properties,
        "digit_sum": digit_sum
    }
