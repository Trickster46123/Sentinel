import hashlib


def password_analyzer():
    password = input("Enter a password to analyze: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    print("\nPassword score:", score, "/ 5")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MODERATE")
    else:
        print("Strength: STRONG")


def hash_file():
    file_path = input("Enter the file path: ")

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        file_hash = hashlib.sha256(file_data).hexdigest()

        print("\nSHA-256 Hash:")
        print(file_hash)

    except FileNotFoundError:
        print("File not found.")


def check_file_integrity():
    file_path = input("Enter the file path: ")
    original_hash = input("Enter the original SHA-256 hash: ")
    if not original_hash.strip():
        print("Error: Please enter an original SHA-256 hash.")
        return

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        current_hash = hashlib.sha256(file_data).hexdigest()

        if current_hash == original_hash.strip().lower():
            print("\nPASS: File integrity verified!")
            print("The hashes match.")

        else:
            print("\nWARNING: File integrity check failed!")
            print("The hashes do not match.")

    except FileNotFoundError:
        print("Error: File not found.")

    except (PermissionError, IsADirectoryError):
        print("Error: Cannot read that file.")

def main():
    while True:
        print("\n========================")
        print("      SENTINEL 0.1")
        print("========================")
        print("1. Password Analyzer")
        print("2. Hash a File")
        print("3. Check File Integrity")
        print("4. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            password_analyzer()

        elif choice == "2":
            hash_file()

        elif choice == "3":
            check_file_integrity()

        elif choice == "4":
            print("Exiting SENTINEL.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()