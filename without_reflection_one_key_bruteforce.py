import string

abc = string.ascii_uppercase


def rotor(lmb, a, m):
    b = (a + m) % 26
    b = lmb[b]
    return (b - m) % 26


def inv(lmb):
    lmb_inv = [0] * len(lmb)
    for i in range(0, len(lmb)):
        lmb_inv[lmb[i]] = i
    return lmb_inv


key = [5]
L1 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
L2 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
Linv = (inv(L1), inv(L2))
cipherText = " "
cipherLen = len(cipherText)
n = len(abc)
message = ''


def compute(letter: int, var: int):
    pos = letter
    ciphIdx = abc.index(cipherText[pos])
    m1 = pos % n
    m2 = (pos - m1) // n % n
    m1 = m1 + key[0]
    m2 = m2 + var
    plnTxt = (ciphIdx + m2) % n
    plnTxt = Linv[1][plnTxt]
    plnTxt = (plnTxt - m2) % n
    plnTxt = (plnTxt + m1) % n
    plnTxt = Linv[0][plnTxt]
    plnTxt = (plnTxt - m1) % n
    messIdx = abc[plnTxt]
    return messIdx


for var in range(0, 26):
    for letter in range(0, len(cipherText)):
        messIdx = compute(letter, var)
        message = (message + messIdx)
    print(message + "\n")
    message = ''
