import sys

def encrypt(message, k):
    encrypted_message = ""
    for char in message.upper():
        if char.isalpha():
            #Remove characters that are not letters
            # Get the ASCII code of the character
            char_code = ord(char)
            
            # Encrypt the character using Caesar cipher
            encrypted_char_code = (char_code - 65 + k) % 26 + 65  # Assuming uppercase letters only
            # Convert the ASCII code back to character
            encrypted_char = chr(encrypted_char_code)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, k):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            # Get the ASCII code of the character
            char_code = ord(char)
            # Decrypt the character using Caesar cipher
            decrypted_char_code = (char_code - 65 - k) % 26 + 65  # Assuming uppercase letters only
            # Convert the ASCII code back to character
            decrypted_char = chr(decrypted_char_code)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <message> <key>")
        sys.exit(1)

    message = sys.argv[1]
    key = int(sys.argv[2])

    encrypted = encrypt(message.upper(), key)
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)



