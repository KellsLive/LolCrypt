#Ceaser Ciper 8/11/2017 By KELS M
#The string to be encrypted/decrypted
message = 'I WILL KILL YOU TONIGHT'

#The encryption key/decryption key
key = 13

#Tells the prpgram to encrypt or decrypt
mode = 'encrypt' #set to 'encrypt' or 'decrypt'

#Every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-=|?><.,\~`'

#Stores the encrypted/decrypted form of the message
translated = ' '

#Capitalize the string in message
message =  message.upper()

#Run the encrypted/decrypted code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        #get the encrypted (or decrypted) number for this symbol
        num  = LETTERS.find(symbol) #get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = - key
        
        
        #Handle the wrap-around if num is larger than the lenght of LETTERS or less than 0
        if num >= len(LETTERS):
            num = - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]

        #Add encrypted/decryptyed number's symbol at the end of translated
    else:
        #Just add thr symbol without encrypting/decrypting
        translated = translated + symbol
#Print the encrypted/decypted string to the screen
print(translated)


