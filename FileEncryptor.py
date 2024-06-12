from caesar_cipher import CaesarCipher
class FileEncryptor:
    def __init__(self, cipher):
        self.cipher = cipher

    def encrypt_file(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            plaintext = f.read()
        encrypted_text = self.cipher.encrypt(plaintext)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

    def decrypt_file(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        decrypted_text = self.cipher.decrypt(ciphertext)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_text)