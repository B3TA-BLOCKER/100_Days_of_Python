alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
text = input("Type your Message : \n").lower()
shift = int(input("Type the shift number : \n"))


# Creating a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):
    cipher_text = ""
    # Inside the 'encrypt' function, shifting each letter of the 'text' forwards in the alphabet by the shift amount 
    # and print the encrypted text.
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position>26:
            new_position -= 26  
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The Encoded text is {cipher_text}")


# Creating a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text , shift_amount):
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount 
    # and print the decrypted text.

    for letter in cipher_text:
        plain_text = ""
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The Decoded text is {plain_text}")


# Checking if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' variable. 

if direction == "encode":
    encrypt(plain_text=text, shift_amount= shift)
elif direction == "decode":
    decrypt(cipher_text=text , shift_amount= shift)