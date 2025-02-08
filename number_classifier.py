ef is_prime(number):
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

def is_perfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number

def is_fun_fact(number):
   armstrong_eq = " + ".join([f"{digit}^{len(str(number))}" for digit in str(number)])  # Use ^ instead of **
   result = is_armstrong(number)
    # Debugging output
   print(f"DEBUG: is_armstrong({number}) -> {result}")

   if result:
        return f"{number} is an Armstrong number because {armstrong_eq} = {number}"
   else:
        return f"{number} is not an Armstrong number"

def classify_number(number: int) -> dict:
    try:
        number = int(number)
    except ValueError:
        return {"number": "alphabet", "error": True}
    
    is_prime_result = is_prime(number)
    is_perfect_result = is_perfect(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")  # Ensure lowercase
    properties.append("odd" if number % 2 != 0 else "even")  # Ensure one of odd/even

    digit_sum = sum(int(digit) for digit in str(number))

    return {
        "number": number,
        "is_prime": is_prime_result,
        "is_perfect": is_perfect_result,
        "properties": properties,  # Ensures ["armstrong", "odd"] if applicable
        "digit_sum": digit_sum
    }
