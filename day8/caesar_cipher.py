alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            position = alphabet.index(char_lower)
            if direction == "encode":
                new_position = (position + shift) % 26
            elif direction == "decode":
                new_position = (position - shift) % 26
            if char.isupper():
                new_text += alphabet[new_position].upper()
            else:
                new_text += alphabet[new_position]
        else:
            new_text += char
    print(f"The {direction}d text is {new_text}")

from cc_art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
