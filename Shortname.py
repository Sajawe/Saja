def shortname(first_name, last_name):
    # Get the first letter of the first name
    first_initial = first_name[0]

    # Get the first 4 letters of the last name, or the entire last name if it's shorter
    shortened_last_name = last_name[:4]

    # Format the short name
    return f"{first_initial}. {shortened_last_name}"

# Main program
if __name__ == "__main__":
    # Prompt the user for first and last names
    first_name = input("First name: ")
    last_name = input("Last name: ")

    # Get the short name
    short_name = shortname(first_name, last_name)

    # Print the result
    print(f"Short name: {short_name}")
