import numpy as np
class TrithemiusCipher:
    def __init__(self, key):
        self.key = key

    def validate_key(self):
        if isinstance(self.key, (list, np.ndarray)):
            if len(self.key) == 2 or len(self.key) == 3:
                return True
        elif isinstance(self.key, str):
            return True
        return False

    def encrypt(self, data):
        if not self.validate_key():
            raise ValueError("Invalid key")

        encrypted_data = []
        if isinstance(self.key, (list, np.ndarray)):
            for i, char in enumerate(data):
                encrypted_char = ord(char) + self.key[i % len(self.key)]
                encrypted_data.append(chr(encrypted_char))
        elif isinstance(self.key, str):
            for i, char in enumerate(data):
                encrypted_char = ord(char) + ord(self.key[i % len(self.key)])
                encrypted_data.append(chr(encrypted_char))
        return ''.join(encrypted_data)

    def decrypt(self, encrypted_data):
        if not self.validate_key():
            raise ValueError("Invalid key")

        decrypted_data = ""
        if isinstance(self.key, (list, np.ndarray)):
            for i, char in enumerate(encrypted_data):
                decrypted_char = ord(char) - self.key[i % len(self.key)]
                decrypted_data += chr(decrypted_char)
        elif isinstance(self.key, str):
            for i, char in enumerate(encrypted_data):
                decrypted_char = ord(char) - ord(self.key[i % len(self.key)])
                decrypted_data += chr(decrypted_char)
        return decrypted_data
