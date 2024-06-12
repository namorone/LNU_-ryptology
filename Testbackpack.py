import unittest
from backpack import *
from backpack_ui import *

class TestKnapsack(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = BackpackCipherApp(self.root)

    def test_generate_sequence(self):
        self.app.generate_sequence()
        sequence = self.app.sequence_value
        self.assertTrue(sequence)

    def test_generate_m(self):
        self.app.generate_m()
        m = self.app.m_value
        self.assertTrue(m)

    def test_generate_t(self):
        self.app.generate_t()
        t = self.app.t_value
        self.assertTrue(t)

    def test_open_file(self):
        # Providing a mock file content
        self.app.file_content = "Test file content"
        self.app.open_file()
        self.assertTrue(self.app.file_content)



    def test_generate_super_increasing_sequence(self):
        sequence, _ = generate_super_increasing_sequence(8)
        self.assertTrue(check_super_increasing_sequence(sequence))

    def test_generate_open_key(self):
        sup_incr_seq = [2, 5, 11, 23, 47, 95, 191, 383]
        m = sum(sup_incr_seq) + random.randint(10, 100)
        t = m * random.randint(2, 10) + 1
        open_key = generate_open_key(sup_incr_seq, m, t)
        self.assertTrue(open_key)

    def test_encrypt_decrypt(self):
        sup_incr_seq = [2, 5, 11, 23, 47, 95, 191, 383]
        m = sum(sup_incr_seq) + random.randint(10, 100)
        t = m * random.randint(2, 10) + 1
        open_key = generate_open_key(sup_incr_seq, m, t)
        text = "Hello, world!"
        ciphertext = encrypt(open_key, text)
        decrypted = decrypt(sup_incr_seq, m, t, ciphertext)
        self.assertEqual(text, decrypted)
