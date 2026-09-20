import hashlib

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