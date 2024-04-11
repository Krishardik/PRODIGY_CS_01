# PRODIGY_CS_01

WiZzryptic is a basic ceaser cipher tool made by me as a part of my internship project to delve into my knowledge in using Python programming for creating cybersecurity-related tools.

The provided code is a Python script implementing the Caesar Cipher algorithm along with a user interface for encryption and decryption. Let's break down its functionality:

**Importing Libraries**: The script imports `pyfiglet` for generating ASCII art and `colorama` for colored output. `colorama.init(autoreset=True)` is used to automatically reset color settings after each print statement.

**Displaying Name**: The `display_name()` function generates ASCII art for the name "WiZzryptic" using `pyfiglet` and prints it in blue color.

**Caesar Cipher Function**: The `caesar_cipher()` function takes three parameters: the text to be encrypted or decrypted, the shift value for the Caesar Cipher, and a boolean flag (`decrypt`) indicating whether to decrypt the text. It iterates over each character in the input text, shifts alphabetic characters based on the given shift value, and leaves non-alphabetic characters unchanged.

**Main Function**: The `main()` function serves as the entry point of the program. It displays a menu with options to encrypt, decrypt, or exit. Depending on the user's choice, it prompts for input messages and shift values, calls the `caesar_cipher()` function accordingly, and displays the encrypted or decrypted message.

**Execution**: The script executes the `main()` function if it's run as the main module (`if __name__ == "__main__": main()`).

This script provides a simple command-line interface for users to encrypt and decrypt messages using the Caesar Cipher algorithm. 



**Steps to Run the tool**

+ *Step 1* : git clone https://github.com/Krishardik/PRODIGY_CS_01
+ *Step 2* : pip install -r requirements.txt
+ *Step 3* : cd PRODIGY_CS_01
+ *Step 4* : python WiZzryptic
