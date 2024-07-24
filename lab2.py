def encrypt(text, key):
    result = []

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            result.append(encrypted_char)
        else:
            result.append(char)

    return ''.join(result)

def decrypt(text, key):
    return encrypt(text, -key)

text = "Endreddy Teja Sai Reddy!"
key = 3		

encrypted_text = encrypt(text, key)
decrypted_text = decrypt(encrypted_text, key)

print(f"Original: {text}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")

