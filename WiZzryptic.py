import pyfiglet
import colorama
from colorama import Fore

# Initialize colorama for colored output
colorama.init(autoreset=True)

def display_name():
    """
    Display the name "WiZzryptic" using figlet.
    """
    # Generating  ASCII art of "WiZzryptic" using the figlet library
    path1 = "figlet-fonts/Graffiti"
    path2 = "figlet-fonts/wideterm"

    ascii_art1 = pyfiglet.figlet_format("WiZzryptic", font=path1, justify = "center")
    ascii_art2 = pyfiglet.figlet_format("Ethical WiZzzrd", font=path2, justify="center")
    # Printing the ASCII art in blue color for better visibility
    print(Fore.YELLOW + ascii_art1)
    print(ascii_art2)

def caesar_cipher(text, shift, decrypt=False):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.

    Args:
    - text (str): The text to be encrypted or decrypted.
    - shift (int): The amount by which the characters are shifted.
    - decrypt (bool): Flag indicating whether to decrypt the text or encrypt it (default: False).

    Returns:
    - str: The encrypted or decrypted text.
    """
    result = ''
    # Iterate over each character in the input text
    for char in text:
        # Check if the character is alphabetic
        if char.isalpha():
            # Determining the starting ASCII value based on the case of the character
            start = ord('a') if char.islower() else ord('A')
            # Apply the Caesar cipher shift and ensure it wraps around the alphabet
            shifted = (ord(char) - start + shift * (-1 if decrypt else 1)) % 26 + start
            # Append the shifted character to the result string
            result += chr(shifted)
        else:
            # Append non-alphabetic characters unchanged
            result += char
    # Return the encrypted or decrypted text
    return result

def main():
    """
    Main function to execute the program.
    """
    # Display the name "WiZzryptic" at the start
    display_name()
    # Start the main program loop
    while True:
        # Display menu options
        print("\nChoose an option:")
        print(Fore.BLUE + "1. Encrypt")
        print(Fore.GREEN + "2. Decrypt")
        print(Fore.RED + "3. Exit")
        # Prompt the user to enter their choice
        choice = input("Enter your choice (1, 2, or 3): ")

        # Process the user's choice
        if choice == '1':
            # Encryption option selected
            message = input("Enter the message to encrypt: ")
            shift = input("Enter the shift value: ")
            if shift.isdigit():
                shift = int(shift)
                # Encrypt the message using the Caesar cipher
                encrypted_message = caesar_cipher(message, shift)
                print("Encrypted message:", encrypted_message)
            else:
                # Invalid shift value entered
                print("Invalid shift value. Please enter a numeric value.")
        elif choice == '2':
            # Decryption option selected
            message = input("Enter the message to decrypt: ")
            shift = input("Enter the shift value: ")
            if shift.isdigit():
                shift = int(shift)
                # Decrypt the message using the Caesar cipher
                decrypted_message = caesar_cipher(message, shift, decrypt=True)
                print("Decrypted message:", decrypted_message)
            else:
                # Invalid shift value entered
                print("Invalid shift value. Please enter a numeric value.")
        elif choice == '3':
            # Exit option selected
            print("Exiting...")
            break
        else:
            # Invalid choice entered
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main ()
