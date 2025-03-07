import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)



# def encrypt(Plain_text, Shift_amount):

#     new_text =""
#     for letter in Plain_text:
#         # print(letter)
#         letter_index = alphabet.index(letter)
#         # print(letter_index)
#         new_text += alphabet[letter_index + Shift_amount]
#     print(f"The encoded text is {new_text}")


# def decrypt(Plain_text, Shift_amount):

#     new_text=""
#     for letter in Plain_text:
#         letter_index = alphabet.index(letter)
#         new_text += alphabet[letter_index - Shift_amount]
#     print(f"The decoded text is {new_text}")

 
def caesar(Start_text, Shift_amount, cypher_direction):
    new_text = ""
    for char in Start_text:
        if char in alphabet:
            position = alphabet.index(char) 
            if cypher_direction == "encode":
                new_text += alphabet[position + Shift_amount]
            elif cypher_direction == "decode":
                new_text += alphabet[position - Shift_amount]
        else:
            new_text += char
    print(f"The {cypher_direction}d text is {new_text}")

re_run = True
while re_run :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(Start_text=text, Shift_amount=shift, cypher_direction=direction)

    re_run = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if re_run == "no":
        re_run=False
        print("GoodBye")