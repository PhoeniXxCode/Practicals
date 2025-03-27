def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:  # If a factor is found, it's not prime
            return False
    return True

# Taking user input
num = int(input("Enter a number: "))

# Analyzing the number
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
