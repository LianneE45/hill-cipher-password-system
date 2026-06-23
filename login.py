#kunci invert matriks
K_INV = [[15, 17],
         [20, 9]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def text_to_numbers(text):
    return [alphabet.index(char) for char in text]

def numbers_to_text(numbers):
    return "".join(alphabet[num] for num in numbers)

def hill_decrypt(ciphertext):
    ciphertext = ciphertext.upper()

    numbers = text_to_numbers(ciphertext)
    
    plaintext_numbers = []
    
    for i in range(0, len(numbers), 2):
        a = numbers[i]
        b = numbers[i + 1]

        p1 = (K_INV[0][0] * a + K_INV[0][1] * b) % 26
        p2 = (K_INV[1][0] * a + K_INV[1][1] * b) % 26

        plaintext_numbers.extend([p1, p2])
    return numbers_to_text(plaintext_numbers)


with open("data.txt", "r") as file:
    original_length = int(file.readline().strip())
    ciphertext = file.readline().strip()

decrypted_password = hill_decrypt(ciphertext)

stored_password = decrypted_password[:original_length]

user_password = input("Masukkan password: ").upper()

if user_password == stored_password:
    print("\nAkses diterima")
else:
    print("\nAkses ditolak")