import random

def check_password_length(password):
    return len(password) >= 9


def perform_security_check(password):
    print("You will be asked for 3 random letters from your password.")

    for _ in range(3):
        position = random.randint(1, len(password))

        user_char = input(f"Enter letter at position {position}: ")

        if user_char != password[position - 1]:
            print("\nSecurity check failed.")
            return False

        print("Correct")

    print("Security check passed.")
    return True
