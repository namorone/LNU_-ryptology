import random
import math


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Виберемо публічний ключ e: 1 < e < phi та gcd(e, phi) == 1
    e = random.randint(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Обчислимо приватний ключ d: (d * e) % phi == 1
    d = pow(e, -1, phi)

    return ((e, n), (d, n))


# Приклад використання:
p = 11
q = 13
public_key, private_key = generate_keypair(p, q)
print("Публічний ключ (e, n):", public_key)
print("Приватний ключ (d, n):", private_key)
def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_msg

# Приклад використання:
plaintext = "Helloюа"
encrypted_msg = encrypt(public_key, plaintext)
print("Зашифроване повідомлення:", encrypted_msg)
def decrypt(private_key, encrypted_msg):
    d, n = private_key
    decrypted_msg = [chr(pow(char, d, n)) for char in encrypted_msg]
    return ''.join(decrypted_msg)

# Приклад використання:
decrypted_msg = decrypt(private_key, encrypted_msg)
print("Розшифроване повідомлення:", decrypted_msg)
