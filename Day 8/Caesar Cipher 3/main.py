from art import logo
# TODO-1: Import and print the logo from art.py when the program starts.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar():
    print(logo)

    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    output_text = ""

    for letter in original_text:

        if letter in alphabet:
            shifted_position = 0
            if encode_or_decode == 'encode':
                shifted_position = alphabet.index(letter) + shift_amount
            if encode_or_decode == 'decode':
                shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")
    try_again = input("Want to try again? Type 'yes' or 'no'.\n").lower()
    if try_again == "yes":
        caesar()


# TODO-3: Can you figure out a way to restart the cipher program?




caesar()



