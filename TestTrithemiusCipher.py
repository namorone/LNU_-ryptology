import unittest
from trithemius_cipher import *
from Attack import *
from UI_Trithemius_Cipher import *

class TestTrithemiusCipher(unittest.TestCase):


    def test_encrypt_decrypt(self):
        plaintext = "Hello, world!"
        key = [3, 5]
        cipher = TrithemiusCipher(key)
        encrypted_text = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(plaintext, decrypted_text)

    def test_build_frequency_table(self):
        text = "hello"
        attack = FrequencyAttack(text)
        expected_frequency_table = {'h': 0.2, 'e': 0.2, 'l': 0.4, 'o': 0.2}
        self.assertEqual(attack.frequency_table, expected_frequency_table)

    def test_find_key(self):
        attack = FrequencyAttack("")
        plaintext = "abc"
        ciphertext = "def"
        expected_key = [3, 3, 3]  # because 'd' - 'a' = 3, 'e' - 'b' = 3, 'f' - 'c' = 3
        self.assertEqual(attack.find_key(plaintext, ciphertext), expected_key)

    def test_active_attack(self):
        attack = FrequencyAttack("")
        plaintext = "abc"
        ciphertext = "def"
        expected_key = [3, 3, 3]
        self.assertEqual(attack.active_attack(plaintext, ciphertext), expected_key)

    def setUp(self):
        self.root = tk.Tk()
        self.app = TrithemiusCipherApp(self.root)

    def test_create_menu(self):
        self.assertIsNotNone(self.app.menu)
        # додаткові перевірки наявності пунктів меню

    def test_create_shift_controls(self):
        self.assertIsNotNone(self.app.shift_frame)
        self.assertIsNotNone(self.app.shift_framel)
        self.assertIsNotNone(self.app.shift_label)
        self.assertIsNotNone(self.app.shift_spinbox)

    def test_get_shift2D(self):
        self.app.shift_spinbox.insert(tk.END, '1,2')
        self.assertEqual(self.app.get_shift(), [1, 2])

    def test_get_shift3D(self):
        self.app.shift_spinbox.insert(tk.END, '1,2,5')
        self.assertEqual(self.app.get_shift(), [1, 2, 5])

    def test_get_shiftStr(self):
        self.app.shift_spinbox.insert(tk.END, 'password')
        self.assertEqual(self.app.get_shift(), 'password')

    def test_create_language_and_action_selectors(self):
        self.assertIsNotNone(self.app.selected_type_action)

    def test_save_text_value(self):
        self.app.input_text.insert(tk.END, "Hello")
        self.app.save_text_value()
        self.assertEqual(self.app.text_value, "Hello")

    def test_create_input_text(self):
        self.assertIsNotNone(self.app.input_text)

    def test_create_output_text(self):
        self.assertIsNotNone(self.app.output_text)

    def test_insert_text(self):
        self.app.insert_text("Test")
        self.assertEqual(self.app.output_text.get("1.0", "end-1c"), "Test")

