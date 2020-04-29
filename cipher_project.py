'''
This encrypt function can be used to encrypt the desired input string by shifting each character along the alphabet by a 
desired shift length.
'''

def encrypt(input_text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    alphabet_up = alphabet.upper()
    for char in input_text:
        if char in alphabet:
            ind = alphabet.find(char)
            output += alphabet[(ind + shift) % 26]
        elif char in alphabet_up:
            ind = alphabet_up.find(char)
            output += alphabet_up[(ind + shift) % 26]
        #This else statement deals with the cases where the character is non-alpha. 
        else:
            output += char
    return output


'''
This decrypt function can be used to decrypt a message that has been encrpyted using the encrypt function. The user must know
the shift value used for the encypted message in order to use this function.
'''

def decrypt(message_text, shift_2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ''
    alphabet_up = alphabet.upper()
    for char_2 in message_text:
        if char_2 in alphabet:
            ind_2 = alphabet.find(char_2)
            decrypted_message += alphabet[(ind_2 - shift_2) % 26]
        elif char_2 in alphabet_up:
            ind_2 = alphabet_up.find(char_2)
            decrypted_message += alphabet_up[(ind_2 - shift_2) % 26]
        #This else statement deals with the cases where the character is non-alpha. 
        else:
            decrypted_message += char_2
    return decrypted_message