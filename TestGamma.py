import unittest
from gamuvanua_cipher import *
from gamma_Ui import *
from PIL import Image

class TestGammaCipher(unittest.TestCase):

    def setUp(self):
        self.crypto_system = GammaCipher()
        self.root = tk.Tk()
        self.app = GammaCipherApp(self.root)

    def test_encrypt(self):
        plaintext = "Hello, World!"
        key = "1010101010"
        encrypted_text = self.crypto_system.encrypt(plaintext, key)
        self.assertNotEqual(plaintext, encrypted_text)  # Перевіряємо, що зашифрований текст не співпадає з оригіналом

    def test_decrypt(self):
        plaintext = "Hello, World!"
        key = "1010101010"
        encrypted_text = self.crypto_system.encrypt(plaintext, key)
        decrypted_text = self.crypto_system.decrypt(encrypted_text, key)
        self.assertEqual(plaintext, decrypted_text)

    def test_vernam_cipher(self):
        plaintext = "Hello, World!"
        key_vernam, encrypted_text_vernam = self.crypto_system.vernam_cipher(plaintext)
        decrypted_text_vernam = self.crypto_system.decrypt(encrypted_text_vernam, key_vernam)
        self.assertEqual(plaintext, decrypted_text_vernam)



    def test_update_language(self):
        self.app.update_language("vernama")
        self.assertEqual(self.app.language, "vernama")

    def test_update_type_action(self):
        self.app.update_type_action("decrypt")
        self.assertEqual(self.app.type_action, "decrypt")

    def test_save_text_value(self):
        self.app.input_text.insert(tk.END, "Test text")
        self.app.save_text_value()
        self.assertEqual(self.app.text_value, "Test text")

    def test_insert_text(self):
        test_text = "Test output text"
        self.app.insert_text(test_text)
        output_text_content = self.app.output_text.get("1.0", "end-1c")
        self.assertEqual(output_text_content, test_text)

    def tearDown(self):
        self.root.destroy()

