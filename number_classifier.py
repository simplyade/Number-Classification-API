def is_prime(number: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    max_divisor = int(number ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    return True

def is_perfect(number: int) -> bool:
    """
    Check if a number is perfect.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if perfect, False otherwise.
    """
    sum_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_divisors == number

def is_armstrong(number: int) -> bool:
    """
    Check if a number is an Armstrong number.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if Armstrong, False otherwise.
    """
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number

def is_fun_fact(number: int) -> str:
    """
    Generate a fun fact about a number.
    
    Args:
        number (int): The number to generate a fun fact for.
    
    Returns:
        str: A fun fact about the number.
    """
    armstrong_eq = " + ".join(f"{digit}^{len(str(number))}" for digit in str(number))
    result = is_armstrong(number)
    if result:
        return f"{number} is an Armstrong number because {armstrong_eq} = {number}"
    else:
        return f"{number} is not an Armstrong number"

def classify_number(number: int) -> dict:
    """
    Classify a number and generate its properties.
    
    Args:
        number (int): to  The number to classify.
    
    Returns:
        dict: A dictionary containing the number's properties.
    """
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
        "digit_sum": digit_sum,
    }
