def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryption & Decryption Tool ===\n")
    
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    action = ""
    while action not in ["E", "D"]:
        action = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    
    if action == "E":
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"\n🔐 Encrypted message: {encrypted}")
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"\n🔓 Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
