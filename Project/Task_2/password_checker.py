import sys
from utils import check_password_length, perform_security_check


def main():
    if len(sys.argv) < 2:
        print("Usage: python password_checker.py passwords.txt")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    for password in passwords:
        print("\nEnter your password:", password)

        if not check_password_length(password):
            print("Password too short.")
            continue

        perform_security_check(password)


if __name__ == "__main__":
    main()
