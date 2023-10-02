class User:
    # Constructor that takes name, email and password
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Function that display the user information once the registration is successful
    def display_user_information(self):
        print()
        print("----User Information----")
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Password: " + self.password)

# Stores user's information
user_database = []

# Function to determine if the user registration is successful
def user_registration():
    # While loop to keep asking user if they want to register another user
    while True:
        print("User Registration: ")
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")

        # loop to iterate over existing user in the database
        for existing_user in user_database:
            # Check if the email already exists,
            if existing_user.email == user_email:
                print("Sorry, this email address is already taken")
                break 

        # If email is unique, prompt user for the password and register the information in the database
        else:
            user_password = input("Enter your password: ")
            new_user = User(user_name, user_email, user_password)
            user_database.append(new_user)
            print("Registration successful!")
            new_user.display_user_information()

        # Ask user if they want to register another user
        another_registration = input("Do you want to register another user? (yes/no): ")
        if another_registration.lower() != "yes":
            break

# Test usage
user_registration()
