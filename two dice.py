import random

def simulate_rolls(num_rolls):
    # Initialize a list to store frequencies of sums from 2 to 12
    # List indices: frequencies[2] will store count of sum 2, ..., frequencies[12] for sum 12
    frequencies = [0] * 13  # Indices 0 and 1 will be unused
    
    # Simulate rolling two dice num_rolls times
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Roll first die (1 to 6)
        die2 = random.randint(1, 6)  # Roll second die (1 to 6)
        dice_sum = die1 + die2        # Sum of the two dice
        frequencies[dice_sum] += 1    # Increment the frequency of this sum
    
    return frequencies

def print_frequency_table(frequencies):
    # Print header
    print("Frequency table (sum, count) for rolling two dice 10000 times")
    
    # Print the frequencies of sums from 2 to 12
    for dice_sum in range(2, 13):  # We only care about sums 2 to 12
        print(f"{dice_sum}: {frequencies[dice_sum]}")

# Main program
if __name__ == "__main__":
    num_rolls = 10000
    frequencies = simulate_rolls(num_rolls)  # Simulate the dice rolls
    print_frequency_table(frequencies)       # Print the frequency table
