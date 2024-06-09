# PRODIGY_CS_01

---

# WiZzryptic

WiZzryptic is a Python script implementing the Caesar Cipher algorithm for encryption and decryption of messages. This tool was developed as part of my internship project to explore Python programming for creating cybersecurity-related tools.

## Overview

The provided Python script allows users to encrypt and decrypt messages using the Caesar Cipher algorithm. Let's break down its functionality:

### Importing Libraries

The script imports pyfiglet for generating ASCII art, colorama for colored output, and regular expressions module re. `colorama.init(autoreset=True)` is used to automatically reset color settings after each print statement.

### Displaying Name

The `display_name()` function generates ASCII art for the name "WiZzryptic" using pyfiglet and prints it in yellow color.

### Caesar Cipher Function

The `caesar_cipher(text, shift, decrypt=False)` function accepts three parameters: the text to be encrypted or decrypted, the shift value for the Caesar Cipher, and a boolean flag (`decrypt`) indicating whether to decrypt the text. It applies the Caesar Cipher algorithm to shift alphabetic characters based on the given shift value while leaving non-alphabetic characters unchanged.

### Main Function

The `main()` function serves as the entry point of the program. It displays a menu with options to encrypt, decrypt, or exit. Depending on the user's choice, it prompts for input messages and shift values, calls the `caesar_cipher()` function accordingly, and displays the encrypted or decrypted message.

### Execution

The script can be executed by running the `WiZzryptic.py` file. It provides a simple command-line interface for users to interact with.

## Usage

### Steps to Run the Tool

1. Clone the repository:
   ```
   git clone https://github.com/Krishardik/WiZzryptic
   ```

2. Navigate to the project directory:
   ```
   cd WiZzryptic
   ```

3. Run the script:
   ```
   python WiZzryptic.py
   ```

## Note

- Ensure to keep your encryption keys secure and share them only with authorized users.
- Use this tool responsibly and ethically in compliance with applicable laws and regulations.
