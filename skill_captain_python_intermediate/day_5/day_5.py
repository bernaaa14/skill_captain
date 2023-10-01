def count_file_lines(filepath):
    # Open the specified file
    with open(filepath, 'r') as file:
        # Read all the lines and store them into variable lines
        lines = file.readlines()
        # Return the number of lines in the file
        return len(lines)
# Test usage
filepath = 'data.txt'
line_count = count_file_lines(filepath)
print(f'Number of lines in the file: {line_count}')