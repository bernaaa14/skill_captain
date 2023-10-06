import re
def check_password_strength(password):
    # If statement to validate the password length of characters
    if 10 <= len(password) <= 15:
        # Search all the occurences of uppercase letter and after that find the length
        uppercase_count = len(re.findall(r"[A-Z]", password))
        # Search all the occurences of lowercase letter and after that find the length
        lowercase_count = len(re.findall(r"[a-z]", password))
        # Search all the occurences of numbers and after that find the length
        numbers_count = len(re.findall(r"[0-9]", password))
        # Search all the occurences of special characters and after that find the length
        special_characters_count = len(re.findall(r"[!@#$%^&*?]", password))

        # Conditional statements to determine score based on elements occurences and return the count
        if numbers_count ==0 and special_characters_count == 0:
            return 1, uppercase_count, lowercase_count, numbers_count, special_characters_count
        elif numbers_count >=1 and special_characters_count >= 1:
            return 5, uppercase_count, lowercase_count, numbers_count, special_characters_count
        else:
            return 3, uppercase_count, lowercase_count, numbers_count, special_characters_count
    else:
        return 0,0,0,0


def main():
    print("-----Welcome to password strength checker-----")
    print(f"Criteria: At least 10 characters maximum 15 (combination of uppercase and lowercase)\nat least 2 numbers "
          "and special characters [!@#$%^&*?] are present")
    print()
    print("Password scoring system:")
    print("Score 1:  No numbers/special characters is present")
    print("Score 3:  A number and a special character is present")
    print("Score 5: All criteria are met")
    print()

    user_password = input("Enter your password: ")
    score, uppercase_count, lowercase_count, numbers_count, special_characters_count = check_password_strength(user_password)

    if score == 0:
        print("Invalid password length. It must be 10-15 characters!")
    else:
        print(f"Your password strength score: {score}")
        print("Your password summary: ")
        print(
            f"Uppercase: {uppercase_count}\nLowercase: {lowercase_count}\nNumbers: {numbers_count}\nSpecial Characters: {special_characters_count}")

if __name__ == "__main__":
    main()
