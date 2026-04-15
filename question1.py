import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase


def shift_letter(letter, shift):
    """
    Shifts a single letter by the given shift value.
    Preserves case (uppercase stays uppercase, lowercase stays lowercase).
    Non-letter characters are returned unchanged.
    """
    if letter.islower():

        index = lower.index(letter)

        return lower[(index + shift) % 26] # Shift the letter and wrap around the alphabet if needed


    if letter.isupper():

        index = upper.index(letter)

        return upper[(index + shift) % 26]


    return letter



def encrypt_text(text, shift1, shift2):
    """
    Encrypts text using shift1 for even positions and shift2 for odd positions.
    """

    encrypted = ""

    for i, letter in enumerate(text):

        if i % 2 == 0:

            encrypted += shift_letter(letter, shift1)

        else:

            encrypted += shift_letter(letter, shift2)

    return encrypted

def decrypt_text(text, shift1, shift2):
    """
    Decrypts text by reversing shift1 and shift2.
    """
    decrypted = ""

    for i, letter in enumerate(text):

        if i % 2 == 0:

            decrypted += shift_letter(letter, -shift1)

        else:

            decrypted += shift_letter(letter, -shift2)

    return decrypted


def verify_files(file1, file2):
    """
    Checks whether the original file and decrypted file match.
    """

    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:

        return f1.read().strip() == f2.read().strip()


def main():
    """
    Runs the encryption, decryption, and verification process.
    """

    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    with open("raw_text.txt", encoding="utf-8") as f:

        original = f.read()

    encrypted = encrypt_text(original, shift1, shift2)

    with open("encrypted_text.txt", "w", encoding="utf-8") as f:

        f.write(encrypted)

    decrypted = decrypt_text(encrypted, shift1, shift2)

    with open("decrypted_text.txt", "w", encoding="utf-8") as f:

        f.write(decrypted)

    if verify_files("raw_text.txt", "decrypted_text.txt"):

        print("SUCCESS: Decryption matches original")

    else:

        print("ERROR: Decryption failed")


if __name__ == "__main__": # Run the program only when this file is executed directly
    main()