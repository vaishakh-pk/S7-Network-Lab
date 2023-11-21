#VAISHAKH.P.K_Substituition Cipher_Server
import socket

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

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening...")
conn, addr = server_socket.accept()
print(f"Connection from {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received:", data)
    key = int(input("Enter key: "))
    #encrypted = caesar_cipher(data, key)
    #print("Encrypted:", encrypted)
    decrypted = caesar_decipher(data, key)
    print("Decrypted:", decrypted)
    #conn.sendall(encrypted.encode())

conn.close()
'''
Output:
Server is listening...
Connection from ('127.0.0.1', 43636)
Received: ofyu
Enter key: 1
Decrypted: next

'''
