import re

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert to lowercase and remove non-letter characters
    cleaned = re.sub(r'[^a-z]', '', s.lower())
    
    # Check if the cleaned string is the same forwards and backwards
    return cleaned == cleaned[::-1]

# Demonstration of how the function works
if __name__ == "__main__":
    test_strings = [
        "Was it a rat I saw?",
        "A nut for a jar of tuna.",
        "Madam",
        "Ni talar bra latin!",
        "Hello, World!"
    ]

    for string in test_strings:
        result = is_palindrome(string)
        print(f'"{string}" is a palindrome: {result}')
