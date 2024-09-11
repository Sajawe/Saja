# Function to read a file and return its content as a list of strings
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines and return them as a list
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

# Function to write a list of strings to a file, line by line
def write_file(lines, file_path):
    with open(file_path, 'w') as file:
        # Write each line from the list to the file
        for line in lines:
            file.write(line)

# Example usage
if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Read from the input file
    file_lines = read_file(input_file)

    # If lines were read successfully, write them to the output file
    if file_lines:
        write_file(file_lines, output_file)
        print(f"Content from '{input_file}' has been successfully written to '{output_file}'.")

