import random


def generate_super_increasing_sequence(n):
    res = []
    cur_sum = 0

    for i in range(n):
        to_add = random.randint(cur_sum + 1, cur_sum + 10)
        res.append(to_add)
        cur_sum += to_add

    return res, cur_sum


def check_super_increasing_sequence(sequence):
    cur_sum = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] <= cur_sum:
            return False
        cur_sum += sequence[i]
    return True, cur_sum


def check_condition(close_key, m, t):
    return check_super_increasing_sequence(close_key)[0] and m > sum(close_key) \
        and (t - 1) % m == 0


def generate_open_key(close_key, m, t):
    if not check_condition(close_key, m, t):
        return None

    return [(x * t) % m for x in close_key]


def to_binary_blocks(text, n):
    res = []
    for ch in text:
        res.append(format(ord(ch), f"0{n}b"))
    return res


def encrypt(open_key, text):
    n = len(open_key)
    res = []
    binary_block_text = to_binary_blocks(text, n)
    for block in binary_block_text:
        res.append(sum([int(block[i]) * open_key[i] for i in range(n)]))
    return res


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def find_inverse(m, t):
    g, x, y = extended_gcd(t, m)
    if g != 1:
        return None
    else:
        return x % m


def decrypt(sup_incr_seq, m, t, ciphertext):
    n = len(sup_incr_seq)
    res = []
    inverse = find_inverse(m, t)
    if inverse is None:
        print("Modular inverse does not exist. Decryption cannot proceed.")
        return None
    for block in ciphertext:
        decrypted_block = ""
        product = (block * inverse) % m
        for i in range(n - 1, -1, -1):
            if product >= sup_incr_seq[i]:
                decrypted_block = "1" + decrypted_block
                product -= sup_incr_seq[i]
            else:
                decrypted_block = "0" + decrypted_block
        res.append(chr(int(decrypted_block, 2)))
    return ''.join(res)


def main():
    sup_incr_seq, sum_ = generate_super_increasing_sequence(8)
    m = sum_ + random.randint(10, 100)
    t = m * random.randint(2, 10) + 1
    open_key = generate_open_key(sup_incr_seq, m, t)

    print(f"Close key: {sup_incr_seq}, sum = {sum_}")
    print(f"m = {m}, t = {t}")
    print(f"Open key: {open_key}")

    text = "hello word?!"
    cipher_text = encrypt(open_key, text)
    decrypted = decrypt(sup_incr_seq, m, t, cipher_text)
    print(f"Text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
