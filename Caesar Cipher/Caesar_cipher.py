from Caesar_cipher_appendix import *

def encrypt(original_text, shift_amount):
    encrypted = ""
    for letter in original_text:
        if letter in alphabet:
            index_original = alphabet.index(letter)
            index_encrypted = index_original + shift_amount
            encrypted += alphabet[index_encrypted]
        else:
            encrypted += letter
    print(f"Here is the encoded result: {encrypted}")

def decrypt(original_text, shift_amount):
    decrypted = ""
    for letter in original_text:
        if letter in alphabet:
            index_original = alphabet.index(letter)
            index_decrypted = index_original - shift_amount
            decrypted += alphabet[index_decrypted]
        else:
            decrypted += letter
    print(f"Here is the decoded result: {decrypted}")

def caesar(direction, text, shift):
    if direction == 'encode':
        encrypt(text,shift)
    if direction == 'decode':
        decrypt(text,shift)
    
print(logo)

more = True
while more == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if again != 'yes':
        print("Bye, Bye!")
        more = False