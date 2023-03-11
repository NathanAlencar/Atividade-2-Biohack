import random
import math

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def mod_inverse(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m

def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    d, n = pk
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

p = 61
q = 53


public_key, private_key = generate_keypair(p, q)

print("Escolha uma opção:")
print("1. Criptografar uma mensagem com a chave pública")
print("2. Descriptografar uma mensagem com a chave privada")
opcao = input("Opção escolhida: ")

if opcao == "1":
    
    message = input("Digite a mensagem a ser criptografada: ")
    ciphertext = encrypt(public_key, message)
    print("Mensagem cifrada:", ciphertext)
elif opcao == "2":
    
    ciphertext = input("Digite a mensagem cifrada: ")
    d = int(input("Digite a chave privada d: "))
    n = int(input("Digite a chave privada n: "))
    private_key = (d, n)
    
    
    plaintext = decrypt(private_key, ciphertext)
    print("Mensagem decifrada:", plaintext)
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")