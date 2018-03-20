def main():
    myMessage = 'Commom sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')

def encryptedMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

    
