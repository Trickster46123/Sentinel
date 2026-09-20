import getpass

def password_analyzer():
    password = getpass.getpass("Enter a sample password to analyze: ")

    length = len(password)
    target = 15

    print("\n==============================")
    print(" SENTINEL PASSWORD ANALYZER")
    print("==============================")

    # Length analysis
    print(f"\nPassword length: {length} characters")

    if length < 8:
        print("Length: Very short")

    elif length < 15:
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

    print("Uppercase:", any(char.isupper() for char in password))
    print("Lowercase:", any(char.islower() for char in password))
    print("Numbers:", any(char.isdigit() for char in password))
    print("Symbols:", any(not char.isalnum() for char in password))

    # Recommendations
    print("\n--- Recommendations ---")

    if length < target:
        remaining = target - length
        print(f"Add at least {remaining} more characters to meet the length target.")

    else:
        print("Length target met. This alone does not guarantee security.")

    print("Use a unique password and avoid predictable patterns.")