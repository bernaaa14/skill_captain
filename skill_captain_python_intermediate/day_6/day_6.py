import random

# List of individual syllables
syllables = ["ka", "li", "ba", "be", "ro", "mo", "ja", "ma", "ai", "vi", "sa"]

# Set to store generated names
generated_names = set()

# Function to generated random name with 3 syllables and avoid generated name duplication
def generate_name():
    while True:
        name = random.choices(syllables, k=3)
        name = "".join(name)
        if name not in generated_names:
            generated_names.add(name)
            return name

# Ask the user to input how many characters they want to generate
num_of_characters = int(input("Enter the number of character names you wnat to generate: "))

# Open file named characters_name.txt in write
characters_name_file = open('characters_name.txt', 'w')

# Generate and write characters into the file
for _ in range(num_of_characters):\
    # Generate a character name using the function generate_name
    character_name = generate_name()

    # Write the character name into the file followed by a new line
    characters_name_file.write(character_name + "\n")


