#VAISHAKH_Hill Cipher_Server
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

def mod_mat_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det %= modulus
    det_inv = -1
    for i in range(1, modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break
    if det_inv == -1:
        raise ValueError("Modular inverse does not exist")
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus
    return matrix_modulus_inv


def decrypt_message(encrypted_text, key):
    size = len(key)
    inverse_key = mod_mat_inv(np.array(key), 26)
    decrypted_matrix = np.dot(text_to_matrix(encrypted_text, size), inverse_key) % 26
    decrypted_text = matrix_to_text(decrypted_matrix)
    return decrypted_text

def receive_message():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print("Server is listening...")

    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    encrypted_message = client_socket.recv(1024).decode()
    return encrypted_message

def main():
    key = [[3, 2], [5, 7]]  # Replace this with your own 2x2 key matrix

    received_message = receive_message()
    decrypted = decrypt_message(received_message, key)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
'''
Output:
Server is listening...
Connection from ('127.0.0.1', 36094) has been established.
Decrypted message: VAISHAKH
'''
