class FrequencyAttack:
    def __init__(self, text):
        self.text = text
        self.frequency_table = self.build_frequency_table()
    def build_frequency_table(self):
        _frequency = {}
        total_characters = len(self.text)
        for char in self.text:
            frequency = self.text.count(char) / total_characters
            _frequency[char] = round(frequency,4)
        return _frequency
    def find_key(self, plaintext, ciphertext):
        key = []
        for i in range(len(plaintext)):
            plaintext_char = plaintext[i]
            ciphertext_char = ciphertext[i]
            # Визначення символу ключа
            key_char = ord(ciphertext_char) - ord(plaintext_char)
            key.append(key_char)
        return key

    def active_attack(self, plaintext, ciphertext):
        key = self.find_key(plaintext, ciphertext)
        return key

    def frequency_analysis_attack(self):
        plaintext = ""
        for char in self.text:
            if char.isalpha():
                plaintext += char

        ciphertext = self.text
        key_length = len(self.find_key(plaintext, ciphertext))
        key = []
        for i in range(key_length):
            ciphertext_chars = [ciphertext[j] for j in range(i, len(ciphertext), key_length)]
            ciphertext_frequency = {char: ciphertext_chars.count(char) / len(ciphertext_chars) for char in
                                    set(ciphertext_chars)}
            sorted_ciphertext_frequency = sorted(ciphertext_frequency.items(), key=lambda x: x[1], reverse=True)
            language_frequency = sorted(self.frequency_table.items(), key=lambda x: x[1], reverse=True)
            mapping = {sorted_ciphertext_frequency[i][0]: language_frequency[i][0] for i in
                       range(min(len(sorted_ciphertext_frequency), len(language_frequency)))}
            key_char = ord(mapping[ciphertext_chars[0]]) - ord(plaintext[i])
            key.append(key_char)

        return key


