def reverse_order():
    numbers = []  # List to store positive integers
    count = 1

    print("Enter positive integers.")
    print("End by giving a negative integer.")

    # Input loop
    while True:
        try:
            num = int(input(f"Integer {count}: "))
            if num < 0:
                break  # Stop if a negative number is entered
            numbers.append(num)  # Add positive number to the list
            count += 1
        except ValueError:
            print("Please enter a valid integer.")

    # Display the number of positive integers
    print(f"Number of positive integers: {len(numbers)}")

    # Reverse the list of numbers and print it
    print(f"In reverse order: {numbers[::-1]}")

# Run the program
if __name__ == "__main__":
    reverse_order()
