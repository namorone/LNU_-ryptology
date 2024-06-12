import random

class GammaCipher:
    def generate_key(self, alphabet, length):
        length += random.randint(0, 10)
        return ''.join(random.choice(alphabet) for _ in range(length))

    def encrypt(self, plaintext, key):
        return ''.join(chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(plaintext))

    def decrypt(self, ciphertext, key):
        return self.encrypt(ciphertext, key)

    def vernam_cipher(self, plaintext):
        key = self.generate_key('01', len(plaintext))
        return key, self.encrypt(plaintext, key)

