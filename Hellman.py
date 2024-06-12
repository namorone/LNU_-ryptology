import random

# Функція для обчислення модулярного піднесення до степеня (a^b) % m
def power_modulo(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

# Генерування випадкового простого числа
def generate_prime_number():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

# Перевірка, чи є число простим
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if power_modulo(a, n - 1, n) != 1:
            return False
    return True

# Генерування випадкового числа для приватного ключа
def generate_private_key():
    return random.randint(2, 100)

# Обчислення відкритого ключа на основі приватного і параметрів p та g
def generate_public_key(private_key, p, g):
    return power_modulo(g, private_key, p)

# Обчислення спільного секретного ключа на основі власного приватного ключа та отриманого від іншого учасника відкритого ключа
def generate_shared_secret(private_key, public_key_received, p):
    return power_modulo(public_key_received, private_key, p)

# Головна функція
def main():
    # Генерування простого числа p та параметру g
    p = generate_prime_number()
    g = random.randint(2, p - 1)

    # Генерування приватного ключа
    private_key_A = generate_private_key()
    private_key_B = generate_private_key()

    # Обчислення відкритих ключів
    public_key_A = generate_public_key(private_key_A, p, g)
    public_key_B = generate_public_key(private_key_B, p, g)

    # Обмін відкритими ключами та обчислення спільних секретних ключів
    shared_secret_A = generate_shared_secret(private_key_A, public_key_B, p)
    shared_secret_B = generate_shared_secret(private_key_B, public_key_A, p)

    # Виведення результатів
    print("Параметр p:", p)
    print("Параметр g:", g)
    print("Приватний ключ А:", private_key_A)
    print("Приватний ключ B:", private_key_B)
    print("Відкритий ключ А:", public_key_A)
    print("Відкритий ключ B:", public_key_B)
    print("Спільний секретний ключ А:", shared_secret_A)
    print("Спільний секретний ключ B:", shared_secret_B)
    return f" Параметр p:{p}\n Параметр g:{g}\n Приватний ключ А:{private_key_A}\n Приватний ключ B:{private_key_B}\n Відкритий ключ А:{public_key_A}\n Відкритий ключ B:{public_key_B}\n Спільний секретний ключ А:{shared_secret_A}\n Спільний секретний ключ B:{shared_secret_B}"

if __name__ == "__main__":
    main()
