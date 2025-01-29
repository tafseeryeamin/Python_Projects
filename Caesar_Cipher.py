alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

def get_valid_direction():
    """Get valid direction input (encode/decode)."""
    while True:
        direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
        if direction in ['encode', 'decode']:
            return direction
        print("Invalid direction! Please type 'encode' or 'decode'.\n")

def get_valid_shift():
    """Get valid shift number (integer)."""
    while True:
        try:
            shift = int(input("Type the shift number: "))
            return shift % 26  # Normalize shift to 0-25
        except ValueError:
            print("Invalid input! Shift must be a number.\n")

def get_valid_message():
    """Get message containing only alphabetic characters."""
    while True:
        message = input("Type the message: ")
        if message.isalpha():
            return message
        print("Error: Message must contain only letters (a-z, A-Z). Try again.\n")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:  # Fixed typo in variable name (was 'lettter')
        # Handle wrap-around using modulo 26 (for letters a-z)
        shifted_position = (alphabet.index(letter) + shift_amount) % 26
        cipher_text += alphabet[shifted_position]
    print(f'Here is your encrypted cipher text: {cipher_text}')

def decrypt(original_text, shift_amount):
    plain_text = ""
    for letter in original_text:
        # Handle wrap-around for negative shifts
        shifted_position = (alphabet.index(letter) - shift_amount) % 26
        plain_text += alphabet[shifted_position]
    print(f'Here is your decrypted text: {plain_text}')

direction = get_valid_direction()
shift = get_valid_shift()
text = get_valid_message()
# Fixed the typo in parameter name (was 'shift_amount')
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid direction choice!")