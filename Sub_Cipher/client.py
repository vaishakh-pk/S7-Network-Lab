#VAISHAKH.P.K_Substituition Cipher_Client

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

while True:
    message = input("Enter message: ")
    if message.lower() == 'exit':
        break
    key = int(input("Enter shift key: "))  # Convert the input key to an integer
    encrypted_text = caesar_cipher(message, key)
    client_socket.sendall(encrypted_text.encode())
    

client_socket.close()

'''
Output:
Enter message: next
Enter shift key: 1
'''

