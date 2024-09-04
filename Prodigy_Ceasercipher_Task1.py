def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)
def encrypt_message(message, shift):
    return caesar_cipher(message, shift)

def decrypt_message(message, shift):
    return caesar_cipher(message, -shift)
def main():
    print("Caesar Cipher")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_message = encrypt_message(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")
if __name__ == "__main__":
    main()

