def print_divisible_numbers():
    count = 0
    for number in range(100, 201):
        # Check if divisible by 4 or 5 but not both
        if (number % 4 == 0 and number % 5 != 0) or (number % 5 == 0 and number % 4 != 0):
            print(number, end=' ')
            count += 1
            # Print a newline after every 10 numbers
            if count == 10:
                print()  # Move to the next line
                count = 0

# Run the function
print_divisible_numbers()