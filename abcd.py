# Function to convert digits into a four-digit number
def get_number(a, b, c, d):
    return a * 1000 + b * 100 + c * 10 + d

# Main function to find the solution
def find_abcd():
    # Iterate over all possible values of A, B, C, D
    for a in range(1, 10):  # A cannot be zero, so range is 1-9
        for b in range(0, 10):  # B can be 0-9
            for c in range(0, 10):  # C can be 0-9
                for d in range(1, 10):  # D cannot be zero, so range is 1-9
                    abcd = get_number(a, b, c, d)
                    dcba = get_number(d, c, b, a)
                    if dcba == 4 * abcd:
                        print(f"The digits are A={a}, B={b}, C={c}, D={d}")
                        print(f"ABCD = {abcd}, DCBA = {dcba}")
                        return

# Run the program
find_abcd()