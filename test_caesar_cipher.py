import unittest
from caesar_cipher import CaesarCipher
from ui import *
from PIL import Image

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        cipher = CaesarCipher(3, 'eng')
        plaintext = "hello"
        expected_encrypted_text = "khoor"
        self.assertEqual(cipher.encrypt(plaintext), expected_encrypted_text)

    def test_decrypt(self):
        cipher = CaesarCipher(3, 'eng')
        ciphertext = "khoor"
        expected_decrypted_text = "hello"
        self.assertEqual(cipher.decrypt(ciphertext), expected_decrypted_text)

    def test_caesar_cipher_image(self):
        # Create a sample image
        image = Image.new("RGB", (100, 100), "white")
        encrypted_image = CaesarCipher(10, 'eng').caesar_cipher_image(image, 10)

        # Check if all pixels are correctly encrypted
        for x in range(image.width):
            for y in range(image.height):
                original_pixel = image.getpixel((x, y))
                encrypted_pixel = encrypted_image.getpixel((x, y))

                # Check if each component of the pixel is shifted correctly
                for i in range(3):  # 3 for RGB components
                    self.assertEqual((original_pixel[i] + 10) % 256, encrypted_pixel[i])

class TestCryptoApp(unittest.TestCase):
    def setUp(self):
        self.app = CryptoApp(tk.Tk())

    def test_update_language(self):
        self.app.update_language('eng')
        self.assertEqual(self.app.language, 'eng')

    def test_update_type_action(self):
        self.app.update_type_action('decrypt')
        self.assertEqual(self.app.type_action, 'decrypt')

    def test_build_frequency_table(self):
        self.app.text_value = "hello"
        table = self.app.build_frequency_table()
        expected_table = {'h': 0.2, 'e': 0.2, 'l': 0.4, 'o': 0.2}
        self.assertDictEqual(table, expected_table)

    def test_brute_force_decrypt(self):

        original_text = "привіт"
        encrypted_text = "туйдкх"
        shift, execution_time = self.app.brute_force_decrypt(original_text, encrypted_text)
        print(shift)
        self.assertEqual(int(shift), 3)

    def test_insert_text(self):
        test_text = "Test text"
        self.app.insert_text(test_text)
        output_text = self.app.output_text.get("1.0", tk.END).strip()
        self.assertEqual(output_text, test_text)

    def test_save_text_value(self):
        self.app.input_text.insert(tk.END, "Test text")
        self.app.save_text_value()
        self.assertEqual(self.app.text_value, "Test text")