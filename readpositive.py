# Function to check if the number is positive and odd
def is_positive_and_odd(n):
    return n > 0 and n % 2 != 0

# Main program logic
def read_positive_and_odd():
    attempts = 0
    max_attempts = 5

    # Loop to ask the user up to five times for a valid number
    while attempts < max_attempts:
        try:
            # Read integer input from the user
            num = int(input("Enter a positive odd integer: "))
            
            # Check if the input is positive and odd
            if is_positive_and_odd(num):
                print(f"Valid input received: {num}")
                return num
            else:
                print("The number is not positive and odd.")
        
        except ValueError:
            # If input is not an integer
            print("Invalid input! Please enter an integer.")
        
        # Increment attempt count
        attempts += 1
    
    print("Too many invalid attempts.")
    return None

# Run the program
read_positive_and_odd()
