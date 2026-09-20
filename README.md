# SENTINEL

A personal cybersecurity toolkit built with Python.

## About the Project

I started SENTINEL because I wanted to build something outside of my college coursework and improve my programming skills.

My goal is to create a useful collection of cybersecurity tools while learning more about Python, file integrity, networking, and security concepts.

Version 0.1 was my first working release. Version 0.2 focuses on improving the password analyzer, adding a secure password generator, and organizing the code into separate files.

## Current Features

### Password Analyzer

The password analyzer checks a password and provides feedback about its length and character types.

Features include:

- A 15-character length target.
- A length gauge showing progress toward the target.
- Detection of uppercase and lowercase letters, numbers, and symbols.
- Specific feedback about password length.
- Recommendations for improving passwords.
- Hidden password input using Python's `getpass` module.

The old five-point scoring system was removed because it didn't give enough information about password security.

The new gauge measures length only. It does not guarantee that a password is secure.

### Secure Password Generator

Version 0.2 introduces a password generator using Python's built-in `secrets` module.

The generator:

- Creates random 20-character passwords.
- Uses uppercase and lowercase letters, numbers, and symbols.
- Uses cryptographically secure randomness.
- Displays the generated password in the terminal.

The generator does not guarantee that every character type will appear in each password.

### SHA-256 File Hasher

Allows users to enter a file path and generate its SHA-256 hash.

A hash acts like a digital fingerprint of a file. It can be used to check whether the file's contents have changed.

### File Integrity Checker

Compares a file's current SHA-256 hash with an original hash provided by the user.

If the hashes match, SENTINEL reports a successful integrity check.

If they differ, SENTINEL displays a warning.

The original hash must come from a trustworthy source.

The program also includes basic error handling for missing files, unreadable files, and empty hash input.

### Interactive Menu

SENTINEL uses a command-line menu that allows users to select different tools without restarting the application.

The menu currently includes:

1. Password Analyzer
2. Hash a File
3. Check File Integrity
4. Generate Secure Password
5. Exit

## Version 0.2 Changes

For this update, I focused on improving the password tools and making the project easier to maintain.

Changes include:

- Increased the password length target from 8 to 15 characters.
- Replaced the old 5/5 score with a length gauge.
- Added more detailed feedback and recommendations.
- Improved the terminal output.
- Added hidden password input.
- Added secure password generation.
- Split the application into separate Python modules.

I also kept the original file tools and tested them to make sure they still worked after reorganizing the code.

## Project Structure

The application is now organized into three Python files:

- `sentinel.py` — Contains the main menu and connects the tools.
- `password_tools.py` — Contains the password analyzer and password generator.
- `file_tools.py` — Contains the file hasher and integrity checker.

Separating the functions makes it easier to update individual tools without having everything in one file.

## How to Run

Requirements:

- Python 3.12 or newer.
- No external Python packages required.

Download or clone the repository, open a terminal in the project folder, and run:

    py sentinel.py

On systems where Python uses the `python` command:

    python sentinel.py

## Testing

I manually tested SENTINEL using sample passwords and text files.

For the password analyzer, I tested empty input, shorter passwords, passwords meeting the length target, and passwords with different character types.

I also tested the secure password generator to confirm that it produces random passwords and returns to the main menu.

For file integrity, I generated an original hash, verified that the unchanged file passed, then modified the file and confirmed that SENTINEL reported a mismatch.

I also tested its handling of nonexistent files.

After separating the code into modules, I tested the original tools again to make sure they still worked.

## Limitations

SENTINEL is currently an educational project.

- Password length and character checks do not guarantee security.
- The analyzer does not currently check against breached password databases or detect predictable patterns.
- Real passwords should not be used when testing the program.
- Generated passwords are displayed in the terminal, so avoid sharing the output.
- File integrity checking does not detect malware.
- The file hasher currently reads the entire file into memory.
- Original hashes must be saved and entered manually.

## Future Development

I'm planning to continue developing SENTINEL as I learn more about Python and cybersecurity.

Some ideas for future versions include:

- Version 0.3: File Guardian, with saved hashes and easier file integrity verification.
- Version 0.4: Network information tools and potentially a basic network map.
- Version 0.5: A graphical user interface.
- Versions 0.6–0.9: Additional features, testing, and improvements based on what the project needs.

The long-term goal is to turn SENTINEL into a more complete and reliable cybersecurity toolkit.

## Project Status

Version 0.1 — Completed and published.

Version 0.2 — Completed and published.

SENTINEL is an ongoing personal project that I'll continue improving as I learn more about programming and cybersecurity.
