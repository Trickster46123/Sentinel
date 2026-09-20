import getpass
import secrets
import string


def password_analyzer():
    password = getpass.getpass("Enter a sample password to analyze: ")

    # Check for empty input
    if not password:
        print("Error: No password entered.")
        return

    length = len(password)
    target = 15

    print("\n==============================")
    print(" SENTINEL PASSWORD ANALYZER")
    print("==============================")

    # Length analysis
    print(f"\nPassword length: {length} characters")

    if length < 8:
        print("Length: Very short")

    elif length < target:
        print("Length: Below target")

    else:
        print("Length: Target met")

    # Length gauge
    filled = min(length, target)

    gauge = "#" * filled + "-" * (target - filled)

    print(f"\nLength Gauge: [{gauge}]")
    print(f"Progress: {length}/{target} characters")

    # Character analysis
    print("\n--- Character Analysis ---")

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if has_upper:
        print("[+] Uppercase letters detected")
    else:
        print("[-] No uppercase letters detected")

    if has_lower:
        print("[+] Lowercase letters detected")
    else:
        print("[-] No lowercase letters detected")

    if has_number:
        print("[+] Numbers detected")
    else:
        print("[-] No numbers detected")

    if has_symbol:
        print("[+] Symbols detected")
    else:
        print("[-] No symbols detected")

    # Recommendations
    print("\n--- Recommendations ---")

    if length < target:
        remaining = target - length
        print(f"[!] Add {remaining} more characters to reach the length target.")

    else:
        print("[+] Length target met.")

    print("Use a unique password for each account.")
    print("Avoid common passwords and predictable patterns.")

    print("\nNote: Length and character checks do not guarantee password security.")


def generate_password():
    length = 20

    alphabet = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )

    print("\n--- Generated Password ---")
    print(password)
    print("--------------------------")