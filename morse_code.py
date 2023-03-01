MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'  ', ',':'--..--'}

def morse_code(word):
    try:
        morse_list = [MORSE_CODE_DICT[letter] for letter in word]
        output_morse = ' '.join(morse_list)
        print(output_morse)
    except:
        print("You have used an unexpected character. Please type your message again")
    finally:
        another_message = input("Would you like to convert another message?  Type Y or N: ").upper()
        if another_message == "Y":
            morse_code(input("Type your message here: ").upper())
        else:
            return

morse_code(input("Type your message here: ").upper())