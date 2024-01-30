import sys

def encrypt(message, k):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - base + k) % 26 + base)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, k):
    # I made the key negative
    return encrypt(message, -k)

if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)

