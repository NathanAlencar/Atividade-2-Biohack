#Tem que instalar a biblioteca no terminal antes - pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_message():
    
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

   
    cipher = AES.new(key, AES.MODE_CBC, iv)

    data = input("Insira a mensagem a ser criptografada: ").encode()


    padded_data = data + b"\0" * (AES.block_size - len(data) % AES.block_size)

    
    encrypted_data = cipher.encrypt(padded_data)

   
    print("Chave: ", key.hex())
    print("IV: ", iv.hex())
    print("Dados criptografados: ", encrypted_data.hex())


def decrypt_message():
    
    key = bytes.fromhex(input("Insira a chave em formato hexadecimal: "))

    iv = bytes.fromhex(input("Insira o IV em formato hexadecimal: "))

    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted_data = bytes.fromhex(input("Insira os dados criptografados em formato hexadecimal: "))

    decrypted_data = decrypt_cipher.decrypt(encrypted_data)

    unpadded_data = decrypted_data.rstrip(b"\0")

    print("Mensagem decifrada: ", unpadded_data.decode())


while True:
    print("Escolha uma opção:")
    print("1 - Criptografar mensagem com chave aleatória")
    print("2 - Descriptografar mensagem com chave fornecida")
    choice = input("Opção: ")

    if choice == "1":
        encrypt_message()
        break
    elif choice == "2":
        decrypt_message()
        break
    else:
        print("Opção inválida. Tente novamente.")