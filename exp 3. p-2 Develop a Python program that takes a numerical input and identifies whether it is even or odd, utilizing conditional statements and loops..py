def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Main program loop
while True:
    # Get user input
    try:
        num = int(input("Enter a number :"))
        check_even_odd(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    # Ask the user if they want to continue
    continue_input = input("Do you want to check another number? (yes/no): ").lower()
    if continue_input != 'yes':
        print("Goodbye!")
        break
