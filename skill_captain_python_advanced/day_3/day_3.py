# Open the file in read mode
file = open("sample.txt", 'r')

# Create our iterator, so we can read each lines from the file
iterator = iter(file)

# While loop to read each line from the file
while True:
    try:
        read_line = next(iterator)
        # Print each line and use the strip function to remove beginning/ending whitespaces
        print(read_line.strip())
        # When StopIteration exception occurs, we have reached the end of the file
        # Break out of the loop
    except StopIteration:
        break
