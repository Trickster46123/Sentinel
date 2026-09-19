\# SENTINEL



\*\*Version 0.1 — Python Cybersecurity Toolkit\*\*



SENTINEL is a personal cybersecurity project I built in Python to practice programming and explore practical security concepts.



The goal is to create a collection of simple security tools that can help users analyze passwords, generate file hashes, and check whether files have changed.



This is my first personal cybersecurity project, and I plan to expand it as I learn more.



\## Features



\### 1. Password Analyzer

\- Checks password length.

\- Checks for uppercase and lowercase letters.

\- Checks for numbers and special characters.

\- Assigns a basic score from 0 to 5.



Note: This is an educational checker. A high score does not guarantee that a password is secure.



\### 2. SHA-256 File Hasher

\- Accepts a file path from the user.

\- Reads the file as binary data.

\- Generates a SHA-256 hash.

\- Displays the hash in hexadecimal format.



\### 3. File Integrity Checker

\- Accepts a file path and an original SHA-256 hash.

\- Calculates the current hash of the file.

\- Compares the two hashes.

\- Reports whether the hashes match.



A mismatch indicates that the file contents differ from the original version.



\### 4. Interactive Menu

\- Allows users to select different tools.

\- Returns to the main menu after each operation.

\- Includes an option to exit the program.



\## Requirements



\- Python 3.12 or newer.

\- No external Python packages required.



SENTINEL uses Python's built-in `hashlib` library.



\## How to Run



1\. Download or clone this repository.

2\. Open PowerShell or a terminal in the project folder.

3\. Run:



```powershell

py sentinel.py

```



On systems where Python is available as `python`, use:



```bash

python sentinel.py

```



\## Example Usage



The main menu displays:



```text

========================

&#x20;     SENTINEL 0.1

========================

1\. Password Analyzer

2\. Hash a File

3\. Check File Integrity

4\. Exit

```



To check file integrity:



1\. Select option 2 to generate a file's SHA-256 hash.

2\. Save the original hash somewhere trustworthy.

3\. Select option 3.

4\. Enter the file path and original hash.

5\. SENTINEL compares the hashes and reports the result.



\## Security and Limitations



\- Use sample passwords for testing. Do not enter real passwords into this educational tool.

\- Password complexity alone cannot guarantee security.

\- File integrity checking requires a trustworthy original hash.

\- Matching hashes do not prove that a file is free from malware.

\- Files are currently loaded into memory, so very large files may be inefficient to process.

\- SENTINEL is an educational project, not a replacement for professional security software.



\## Future Plans



Potential features for future versions:



\- Local network information and visualization.

\- Improved password analysis.

\- Better input validation.

\- File hashing in chunks for large files.

\- Graphical user interface.



\## Project Status



Version 0.1: Core functionality implemented and manually tested.



This project is actively being developed as I continue learning Python and cybersecurity.

