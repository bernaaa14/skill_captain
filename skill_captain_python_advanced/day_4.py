# authorization decorator that takes function as an argument
def authorization(func):
    # Provide the list of authorized usernames
    authorized_usernames = ["bernaaa14", "shamkhizou", "pipithebabycat"]

    # Inner function to check if the provided username is in authorized usernames
    def wrapper(username):
        if username in authorized_usernames:
            # Calls the function passed once authorized
            func()
        else:
            # Display a message when the provided username is not in the authorized list
            print("Unauthorized!")

    return wrapper

# authorization decorator to wrap the greetings func
@authorization
def greetings():
    print("Congratulations! you are one of the few people that have access to this function")

# Test usage
# Ask for user for their username
username_input = input("Enter the username ")
# pass the input into the greetings function to be used as an argument in the wrapper function
greetings(username_input)
