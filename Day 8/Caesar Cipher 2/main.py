alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# def decrypt(encrypted_word, shift_amount):
#     deciphered_text = ""
#     for letter in encrypted_word:
#         shifted_position = alphabet.index(letter) - shift_amount
#         deciphered_text += alphabet[shifted_position]
#     print(f"Here is the decrypted text: {deciphered_text}")
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

def caesar(original_text, shift_amount, direction_of_encryption):
    changed_text = ""
    for letter in original_text:
        shifted_position = 0
        if direction_of_encryption == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
        if direction_of_encryption == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        changed_text += alphabet[shifted_position]
    if direction_of_encryption == "encode":
        print(f"Here is the encoded result: {changed_text}")
    if direction_of_encryption == "decode":
        print(f"Here is the decoded result: {changed_text}")


caesar(text, shift, direction)



