# This program implements a custom encryption and decryption scheme based on character shifts. It reads text from a file, applies specific transformations to the characters based on their case and position in the alphabet, and writes the encrypted and decrypted results to separate files. The program also includes a verification step to ensure that the decrypted text matches the original raw text.
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def shift_letter(letter, shift):
  position=ord(letter)-ord('a')
  new_position=(position+shift)%26
  return chr(new_position +ord('a'))

def shift_letter_upper(letter, shift):
    position=ord(letter)-ord('A')
    new_position=(position+shift)%26
    return chr(new_position +ord('A'))

def encrypt_char(char, shift1, shift2):
  if char.islower() and 'a' <= char <= 'm':
    return shift_letter(char, shift1 * shift2) 
  if char.islower() and 'n'<=char<='z':
    return shift_letter(char, -(shift1+shift2))
  if char.isupper() and 'A'<=char<='M':
    return shift_letter_upper(char, -shift1)
  if char.isupper() and 'N'<=char<='Z':
    return shift_letter_upper(char, shift2**2)
  else:
    return char
  
def encrypt(shift1, shift2):
    with open('raw_text.txt', 'r') as f:
      content=f.read()

    encrypted=''
    for char in content:
      encrypted += encrypt_char(char, shift1, shift2)

    with open("encrypted_text.txt","w") as f:
      f.write(encrypted)

def decrypt_char(char, shift1, shift2):
    if char.islower() and 'a'<=char<='m':
      return shift_letter(char, -shift1 * shift2) 
    if char.islower() and 'n'<=char<='z':
      return shift_letter(char, shift1 + shift2)
    if char.isupper() and 'A'<=char<='M':
      return shift_letter_upper(char, shift1)
    if char.isupper() and 'N'<=char<='Z':
      return shift_letter_upper(char, -shift2**2)
    else:
      return char

def decrypt(shift1, shift2):
    with open('encrypted_text.txt', 'r') as f:
        content=f.read()
      
    decrypted=''
    for char in content:
        decrypted +=decrypt_char(char,shift1,shift2)

    with open('decrypted.txt','w') as f:
        f.write(decrypted)

def verify():
    with open('raw_text.txt', 'r') as f:
        raw_text=f.read()

    with open('decrypted.txt', 'r') as f:
        decrypted_text=f.read()

    if raw_text==decrypted_text:
        print("Success! The files match.")
    else:
        print("Uh oh! The files do not match.")

def main():
    shift1=int(input("Enter shift1: "))
    shift2=int(input("Enter shift2: "))
    encrypt(shift1, shift2)
    decrypt(shift1, shift2)
    verify()
    
if __name__ == "__main__":
    main()