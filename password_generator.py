import random
import string

while True:

    print("\n===== PASSWORD GENERATOR =====")
    print("1. Generate Password")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        length = int(input("Enter password length: "))
        count = int(input("How many passwords do you want to generate? "))

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        print("\nGenerated Passwords:")

        for i in range(count):

            password = ""

            for j in range(length):
                password += random.choice(characters)

            print(f"\nPassword {i+1}: {password}")

            # Password Strength Checker
            if length < 8:
                strength = "Weak"
            elif length < 12:
                strength = "Medium"
            else:
                strength = "Strong"

            print("Strength:", strength)

    elif choice == 2:

        print("Thank you for using Password Generator!")
        break

    else:

        print("Invalid Choice!")