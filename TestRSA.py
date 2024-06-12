import unittest
from rsa_ui import *

class TestRSA(unittest.TestCase):
    def test_generate_keypair(self):
        p = 61
        q = 53
        public_key, private_key = generate_keypair(p, q)
        self.assertTrue(public_key != private_key)
        # Перевіряємо, що e та d є взаємно оберненими за модулем phi
        self.assertEqual((public_key[0] * private_key[0]) % ((p - 1) * (q - 1)), 1)

    def test_encrypt_decrypt(self):
        p = 61
        q = 53
        public_key, private_key = generate_keypair(p, q)
        plaintext = "Helloюа"
        encrypted_msg = encrypt(public_key, plaintext)
        decrypted_msg = decrypt(private_key, encrypted_msg)
        self.assertEqual(plaintext, decrypted_msg)

    def test_long_message(self):
        p = 61
        q = 53
        public_key, private_key = generate_keypair(p, q)
        plaintext = "This is a very long message. It contains many characters and symbols, including spaces, commas, periods, and even Unicode characters like э, ю, and а. The message is long enough to test the RSA encryption and decryption functions with various edge cases."
        encrypted_msg = encrypt(public_key, plaintext)
        decrypted_msg = decrypt(private_key, encrypted_msg)
        self.assertEqual(plaintext, decrypted_msg)

    def test_empty_message(self):
        p = 61
        q = 53
        public_key, private_key = generate_keypair(p, q)
        plaintext = ""
        encrypted_msg = encrypt(public_key, plaintext)
        decrypted_msg = decrypt(private_key, encrypted_msg)
        self.assertEqual(plaintext, decrypted_msg)