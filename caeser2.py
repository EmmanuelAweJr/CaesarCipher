

THE_CHAR_CODE = 90 #accoring to the ASCII chart
THE_CHAR_RANGE = 26

def cipher_shift(message, shift):
    # result
    Final = ""

    for char in message.upper():
        #Remove characters that are not letters
        if char.isalpha():

            #Convert characrerter to ASCII code
            char_code =  ord(char)
    
            new_char_code = char_code + shift

            if new_char_code > THE_CHAR_CODE:
                new_char_code -= char_code + shift

            Final_char = chr(new_char_code)

            Final += Final_char #shortcut for Final + Final_char
        else:
            Final += char # "+=" is a shortcut for Final = Final + Char

    #print(char, char_code, new_char_code, Final_char)
    print(Final)

cipher_shift("Hello World", 7)


