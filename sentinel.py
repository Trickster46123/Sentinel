from password_tools import password_analyzer, generate_password
from file_tools import hash_file, check_file_integrity


def main():
    while True:
        print("\n========================")
        print("      SENTINEL 0.2")
        print("========================")
        print("1. Password Analyzer")
        print("2. Hash a File")
        print("3. Check File Integrity")
        print("4. Generate Secure Password")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            password_analyzer()

        elif choice == "2":
            hash_file()

        elif choice == "3":
            check_file_integrity()

        elif choice == "4":
            generate_password()

        elif choice == "5":
            print("Exiting SENTINEL.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()