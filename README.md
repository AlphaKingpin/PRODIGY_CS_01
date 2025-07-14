# Caesar Cipher Encryption & Decryption Tool

This Python script allows you to encrypt and decrypt text using the classic Caesar Cipher algorithm. It's a simple substitution cipher where each letter in the plaintext is shifted a fixed number of positions down or up the alphabet.

## Features

- Encrypt or decrypt any message using a shift key
- Supports both uppercase and lowercase letters
- Retains spaces, punctuation, and symbols
- Clean and interactive CLI (Command Line Interface)
- Handles invalid inputs gracefully

## How It Works

The Caesar Cipher works by shifting the letters of a message by a fixed number. For example, with a shift of 3:
A → D  
B → E  
C → F  
...

Decryption reverses the shift.

## Usage Instructions

1. Run the script using Python 3:
   ```bash
   python3 ceasercypher.py
   ```

2. Follow the prompts:
   - Enter the message you want to encrypt or decrypt.
   - Enter the shift value (e.g., 3).
   - Choose 'E' to encrypt or 'D' to decrypt.

### Example

```
Enter your message: This is one of my good Python works, Yaaay to me
Enter shift value (e.g., 3): 3
Type 'E' to Encrypt or 'D' to Decrypt: E

Encrypted message: Wklv lv rqh ri pb jrrg Sbwkrq zrunv , Bdddb wr ph
```

```
Enter your message: Wklv lv rqh ri pb jrrg Sbwkrq zrunv , Bdddb wr ph
Enter shift value (e.g., 3): 3
Type 'E' to Encrypt or 'D' to Decrypt: D

Decrypted message: This is one of my good Python works, Yaaay to me
```

## File Structure

```
ceasercypher.py        # Main script file
ceasercypherresults.png  # Screenshot of program output
README.md              # This documentation
```

## Requirements

- Python 3.x  
(No external libraries required)

## Author

Thywill Essel  
Innovative Male Entrepreneur | Python Developer | Founder of The WORD Expertise
