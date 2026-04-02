
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(encode_decode,original_text,shift_amount):
        shift_var = ""
        for i in range(len(original_text)):
            if original_text[i] in alphabet:
                pos = alphabet.index(original_text[i])
                if(encode_decode=="decode"):
                    shifted = (pos - shift_amount) % 26
                if (encode_decode == "encode"):
                    shifted = (pos + shift_amount) % 26
                shift_var += alphabet[shifted]
            else:
                shift_var += original_text[i]

        if (encode_decode == "decode"):
            print("The decoded value is: ")
        if (encode_decode == "encode"):
            print("The encoded value is: ")
        print(shift_var)
inp="yes"
while inp=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    inp=input("Type yes if you want to go again.Otherwise type no")