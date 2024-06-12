class CaesarCipher:
    def __init__(self, shift, language):
        self.shift = shift
        self.language = language.lower()

        if self.language not in ['ukr', 'eng']:
            raise ValueError("Підтримуються лише 'ukr' та 'eng' як мови.")

        if self.language == 'ukr':
            self.alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        elif self.language == 'eng':
            self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.lower() in self.alphabet:
                if char.islower():
                    shifted = self.alphabet[(self.alphabet.index(char) + self.shift) % len(self.alphabet)]
                elif char.isupper():
                    shifted = self.alphabet[(self.alphabet.index(char.lower()) + self.shift) % len(self.alphabet)].upper()
                encrypted_text += shifted
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.lower() in self.alphabet:
                if char.islower():
                    shifted = self.alphabet[(self.alphabet.index(char) - self.shift) % len(self.alphabet)]
                elif char.isupper():
                    shifted = self.alphabet[(self.alphabet.index(char.lower()) - self.shift) % len(self.alphabet)].upper()
                decrypted_text += shifted
            else:
                decrypted_text += char
        return decrypted_text


    def caesar_cipher_image(self, image, shift):
        #  шифрування/розшифрування для кожного пікселя зображення
        encrypted_image = image.copy()
        for x in range(image.width):
            for y in range(image.height):
                pixel = image.getpixel((x, y))
                encrypted_pixel = tuple([(component + shift) % 256 for component in
                                         pixel])
                encrypted_image.putpixel((x, y), encrypted_pixel)
        return encrypted_image




