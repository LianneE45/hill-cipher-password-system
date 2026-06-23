#kunci matrix
K = [[3, 3],
     [2, 5]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def text_to_numbers(text):
    return [alphabet.index(char) for char in text]


def numbers_to_text(numbers):
    return "".join(alphabet[num] for num in numbers)


def hill_encrypt(text):
    text = text.upper()

    text = text.replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    numbers = text_to_numbers(text)

    ciphertext_numbers = []

    for i in range(0, len(numbers), 2):
        a = numbers[i]
        b = numbers[i + 1]

        c1 = (K[0][0] * a + K[0][1] * b) % 26
        c2 = (K[1][0] * a + K[1][1] * b) % 26

        ciphertext_numbers.extend([c1, c2])

    return numbers_to_text(ciphertext_numbers)



password = input("Buat Password(huruf): ").upper()

original_length = len(password)

ciphertext = hill_encrypt(password)

with open("data.txt", "w") as file:
    file.write(str(original_length) + "\n")
    file.write(ciphertext)

print("\nPassword berhasil disimpan.")
print("Encrypted password:", ciphertext)