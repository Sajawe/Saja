# Function to get input from the user and print it as a quote
def quote_text():
    # Get the input from the user
    text = input("Write a line of text: ")
    
    # Print the text as a quote
    print(f'Quote: ”{text}”')

# Call the function when the script is executed
if __name__ == "__main__":
    quote_text()
