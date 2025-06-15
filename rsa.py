import random as rd


p = int(input("Donner p : "))
q = int(input("Donner q : "))

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def calculer_n(p, q):
    return p * q

def calculer_phi(p, q):
    return (p - 1) * (q - 1)


def generate_cle_e(phi_n):
    valeurs_communes = [3, 17, 257, 65537]
    for e in valeurs_communes:
        if e < phi_n and pgcd(e, phi_n) == 1:
            return e
    while True:
        e = rd.randint(3, phi_n - 1)
        if pgcd(e, phi_n) == 1:
            return e


def euclide_etendu(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = euclide_etendu(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y


def generate_cle_d(e, phi_n):
    gcd, x, y = euclide_etendu(e, phi_n)
    return (x % phi_n + phi_n) % phi_n

# Chiffrement
def encrypt_rsa(message, n_val, e):
    encrypted_message = []
    for char in message:
        char_value = ord(char)
        encrypted_char = pow(char_value, e, n_val)
        encrypted_message.append(encrypted_char)
    return encrypted_message

# Déchiffrement
def decrypt_rsa(encrypted_message, n_val, d):
    message = ''
    for encrypted_char in encrypted_message:
        decrypt_code = pow(encrypted_char, d, n_val)
        char = chr(decrypt_code)
        message += char
    return message

phi_n = calculer_phi(p, q)
n_val = calculer_n(p, q)
e = generate_cle_e(phi_n)
d = generate_cle_d(e, phi_n)


message_clair = input("Entrez un message à chiffrer : ")


chiffre = encrypt_rsa(message_clair, n_val, e)


message_dechiffre = decrypt_rsa(chiffre, n_val, d)


print(f"p = {p}, q = {q}")
print(f"n = {n_val}, φ(n) = {phi_n}")
print(f"Clé publique : (e={e}, n={n_val})")
print(f"Clé privée : d={d}")
print(f"Message chiffré : {chiffre}")
print(f"Message déchiffré : {message_dechiffre}")