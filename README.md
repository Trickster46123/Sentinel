# SENTINEL

A personal cybersecurity toolkit built with Python.

## About the Project

I started SENTINEL because I wanted to build something outside of my college coursework and improve my programming skills.

My goal is to create a useful collection of cybersecurity tools while learning more about Python, file integrity, networking, and security concepts.

Version 0.1 is the first working release. It focuses on password analysis and file integrity.

## Current Features

### Password Analyzer

Checks a password for:
- Length of at least 8 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

It gives the password a score out of 5.

This is a basic educational tool, not a guarantee that a password is secure.

### SHA-256 File Hasher

Allows users to enter a file path and generate its SHA-256 hash.

A hash acts like a digital fingerprint of a file. It can be used to check whether the file's contents have changed.

### File Integrity Checker

Compares a file's current SHA-256 hash with an original hash provided by the user.

If the hashes match, SENTINEL reports a successful integrity check.

If they differ, SENTINEL displays a warning.

The original hash must come from a trustworthy source.

### Interactive Menu

SENTINEL uses a command-line menu that allows users to select tools and return to the main menu without restarting the application.

## How to Run

Requirements:
- Python 3.12 or newer
- No external Python packages

Download or clone the repository, open a terminal in the project folder, and run:

    py sentinel.py

On systems where Python uses the `python` command:

    python sentinel.py

## Testing

I manually tested the program using sample passwords and text files.

For file integrity, I generated an original hash, verified that the unchanged file passed, then modified the file and confirmed that SENTINEL reported a mismatch.

I also tested its handling of nonexistent files.

## Limitations

SENTINEL is currently an educational project.

- Password scoring does not guarantee security.
- Real passwords should not be entered for testing.
- File integrity checking does not detect malware.
- The file hasher currently reads the entire file into memory.
- Original hashes must be saved and entered manually.

## Future Development

I'm planning to continue developing SENTINEL.

Some ideas for future versions include:
- Saving original file hashes for future checks.
- Improved password analysis.
- Network information tools.
- A network visualization feature.
- A graphical interface.

The next goal is version 0.2, which will focus on improving file integrity checking.

## Project Status

Version 0.1 — Completed and published.

This is an ongoing personal project that I'll continue improving as I learn more about programming and cybersecurity.

