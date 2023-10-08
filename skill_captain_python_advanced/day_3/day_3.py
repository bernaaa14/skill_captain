# Open the file in read mode
file_name = open("sample.txt", 'r')

# Create our iterator, so we can read each lines from the file
iterator = iter(file_name)
# Variable to track if we reach the end of file
end_of_file = False

# While loop to continue until the end of the file is reached
while not end_of_file:
    try:
        # Read next line of the file using the iterator function
        next_line = next(iterator)
        print(next_line.strip())  # Use strip() to remove leading/trailing whitespace and newlines
        # When StopIteration exception occurs, we have reached the end of the file
        # exit the loop
    except StopIteration:
        end_of_file = True
