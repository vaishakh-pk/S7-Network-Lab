#VAISHAKH_Hill Cipher_Client
import socket
import numpy as np

def text_to_matrix(text, size):
    text = text.upper().replace(" ", "")
    padding = size - len(text) % size if len(text) % size != 0 else 0
    text += 'X' * padding
    matrix = [ord(char) - 65 for char in text]
    return np.array(matrix).reshape(-1, size)

def matrix_to_text(matrix):
    text = ''.join([chr(int(val) + 65) for val in matrix.flatten()])
    return text

def encrypt_message(plain_text, key):
    size = len(key)
    plain_matrix = text_to_matrix(plain_text, size)
    key_matrix = np.array(key)
    encrypted_matrix = np.dot(plain_matrix, key_matrix) % 26
    encrypted_text = matrix_to_text(encrypted_matrix)
    return encrypted_text

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    print("Connected to server.")

    client_socket.send(message.encode())
    client_socket.close()

def main():
    key = [[3, 2], [5, 7]]  # Replace this with your own 2x2 key matrix
    message_to_encrypt = input("Enter the message :")  # Replace this with your message

    encrypted_message = encrypt_message(message_to_encrypt, key)
    print("Encrypted message:", encrypted_message)

    send_message(encrypted_message)

if __name__ == "__main__":
    main()
'''
Output:
Enter the message :VAISHAKH
Encrypted message: LQKMVONR
Connected to server.

'''
