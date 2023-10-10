import string
abc = string.ascii_uppercase


def rotor(lmb, a, m):  # encrypt with the rotor
    b = (a + m) % 26
    b = lmb[b]
    return (b - m) % 26


def inv(lmb):  # inverting permutation:
    lmb_inv = [0] * len(lmb)
    for i in range(0, len(lmb)):
        lmb_inv[lmb[i]] = i
    return lmb_inv


key = [19, 3]
L1 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
L2 = [10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
Linv = (inv(L1), inv(L2))
cipherText = " "
cipherLen = len(cipherText)
n = len(abc)
message = ''

for letter in range(0, len(cipherText)):
    pos = letter
    ciphIdx = abc.index(cipherText[pos])
    m1 = pos % n
    m2 = (pos - m1) // n % n
    m1 = m1 + key[0]
    m2 = m2 + key[1]
    plnTxt = (ciphIdx + m2) % n
    plnTxt = Linv[1][plnTxt]
    plnTxt = (plnTxt - m2) % n
    plnTxt = (plnTxt + m1) % n
    plnTxt = Linv[0][plnTxt]
    plnTxt = (plnTxt - m1) % n
    messIdx = abc[plnTxt]
    message = (message + messIdx)

print(message)
