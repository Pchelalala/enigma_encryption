class EnigmaMachine:
    def __init__(self, rotor1, rotor2, reflector, key):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.reflector = reflector
        self.rotor1_position = key[0]
        self.rotor2_position = key[1]

    def rotate_rotors(self):
        self.rotor1_position = (self.rotor1_position + 1) % 26
        if self.rotor1_position == self.rotor1.index(0):
            self.rotor2_position = (self.rotor2_position + 1) % 26

    def encrypt_letter(self, letter):
        letter_idx = ord(letter) - ord('A')
        letter_idx = (letter_idx + self.rotor1_position) % 26
        letter_idx = self.rotor1[letter_idx]
        letter_idx = (letter_idx - self.rotor1_position + self.rotor2_position) % 26
        letter_idx = self.rotor2[letter_idx]
        letter_idx = (letter_idx - self.rotor2_position) % 26
        letter_idx = self.reflector[letter_idx]
        letter_idx = (letter_idx + self.rotor2_position) % 26
        letter_idx = self.rotor2.index(letter_idx)
        letter_idx = (letter_idx - self.rotor2_position + self.rotor1_position) % 26
        letter_idx = self.rotor1.index(letter_idx)
        letter_idx = (letter_idx - self.rotor1_position) % 26
        return chr(letter_idx + ord('A'))

    def decrypt(self, ciphertext):
        plaintext = ''
        for letter in ciphertext:
            if letter.isalpha():
                plaintext += self.encrypt_letter(letter)
                self.rotate_rotors()
            else:
                plaintext += letter
        return plaintext

def main():
    rotor1 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
    rotor2 = [10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
    reflector = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
    key = [15, 20]

    enigma = EnigmaMachine(rotor1, rotor2, reflector, key)

    ciphertext = "OFCCDMDDVAHQBPNDXKGVFXSKNDOGXNKDVQGEXYAAXTOAVRPMJUOXTNZVREZEMQFWGRMOTNHTCWKZELUREAHLCNAOEKUJHFXIUGGIFVFTRMNOQAGBGRKVESAFVIBARRMNXMAHKRFHFLYROWUIPIGEZWQEBQMNKZSMJONCVLLZGOSYLAFQIIHYIEEJCTJGGSCVOPHXRPAUIXJLCCKMKGAXXVAJUPMJPLVYXHLPDVFMYGVCZYKIMCOHXMCPIEWYULDZZEKBWMUOLEHXXVKANOADICMUOPWSQAWBTJKMCHMOQCNUSYRUYUMISEMBZJCHQRQTHLBGFCBLMDVKMPLYWZKEDGTQCERCRHYJKNCREOTKGCZLBQPIBQWBJABKZHFAPQNJUSWXFWUGBXXDXATCRVILJTLXLHLEJNGLRDLAKIJNHKNWXZJJYWPUSSIVZHECYPXUJFLXFAUGJPVSWHSBSJKJUUMYEXMAYVUWLQPSWMFOEDAICOSFXWQMIPIJKZLQATFWSQEPKRGSRGVPQQVWSEDPHWUJDERJPSSLGCGDPYDBSNKBTURYPFRTHNHTHMXKICTNMTFUQGXURQTCVJRRTLXDKWZYHTJEQYCZMNBYPTNQVWLFTVCTWDZNCHBDOAOVEZLBZM"
    plaintext = enigma.decrypt(ciphertext)
    print("Decrypted Text:")
    print(plaintext)

if __name__ == "__main__":
    main()
