import numpy as np
import math
from numpy import linalg as LA

# def gcd(a, b):
#     r1 = a
#     r2 = b
#     s1 = 1
#     s2 = 0
#     t1 = 0
#     t2 = 1
#     r = r1%r2
#     while r != 0:
#         q = r1//r2
#         s = s1 - q * s2
#         t = t1 - q * t2
#         r1 = r2
#         r2 = r
#         s1 = s2
#         s2 = s
#         t1 = t2
#         t2 = t
#         r = r1 % r2
#     r = r2
#     s = s2
#     t = t2
#     return r, s, t
#
#
# keyA = []
# check = 0
# while check == 0:
#     a = np.random.randint(0, 26, size=(4, 4))
#     d = LA.det(a)
#     if d > 0:
#         nsd, x, y = gcd(d, 26)
#         if nsd == 1:
#             keyA = a
#             print("Key A:", keyA)
#             print("det :", d)
#             check = 1
# b = np.random.randint(0, 26, size=(4, 1))
# print(b)
# LA.det(a)
# print(LA.det(a))


keyA = [[15, 11, 9, 24],
        [2, 0, 1, 7],
        [14, 10, 25, 10],
        [25, 6, 16, 21]]
print(np.linalg.det(keyA))

# w=17877
# НСД(17877, 26)=1


keyS = [5,
        21,
        11,
        14]
# n=26


# input our text in file and correct it a little
with open('input_aff.txt', 'r') as file:
    sentence = file.read().replace(' ', '').upper().replace('\n', '')
print(sentence)

# initialize array for input text
input_text = []


# make string look like 2d arr
def ArrTxt2D(txt):
    text = list(txt)
    print("length of text is ", len(text))
    while len(text) % 4 != 0:
        text.append('Z')
    amount = len(text) / 4
    print(1, amount)
    for i in range(int(amount)):
        a = []
        for j in range(4):
            a.append(text[0])
            text = text[1:]
        input_text.append(a)


ArrTxt2D(sentence)
print(input_text)


# translate character to ASCII
def chrToOrd(txt):
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            txt[i][j] = (ord(txt[i][j]) - ord('A')) % 26


chrToOrd(input_text)
print("ASCII code of characters: ")
for i in range(len(input_text)):
    print(input_text[i])

print()

# transpose 2d matrix(rows becomes columns)
transpose_arr = []
for i in np.transpose(input_text):
    transpose_arr.append(list(i))
print("Transposed matrix of chars: ")
for i in range(len(transpose_arr)):
    print(transpose_arr[i])

# encoding ASCII array(multiply this arr on keyA)
message = []
for i in input_text:
    message.append(list(i))
print("message ", message)

a = np.array(keyA)
print("a", a)
m = np.array(message)
print("m", m)
encoded_A = []  # res of multiplying a on m
for i in range(len(message)):
    res = np.matmul(a, m[i]) % 26
    print(res)
    encoded_A.append(list(res))
encoded =[]
for i in np.transpose(encoded_A):
    encoded.append(list(i))
print("After multiplying on key A:")
for i in range(len(encoded_A)):
    print(encoded_A[i])

# add keyS to encoded_A arr
for i in range(len(encoded[0])):
    for j in range(len(encoded)):
        encoded[j][i] = (encoded[j][i] + keyS[j]) % 26
print("After adding key S:")
for i in range(len(encoded)):
    print(encoded[i])


# return ASCII code to chr
def ordToChr(txt):
    encoded_res = []
    for i in range(len(txt)):
        res = []
        for j in range(len(txt[i])):
            res.append(chr(txt[i][j] + ord('A')))
        encoded_res.append(res)
    return encoded_res


chr_arr = ordToChr(encoded)
print("Encrypted text in character respresentation: ")
for i in range(len(chr_arr)):
    print(chr_arr[i])

# writting result of encoded text in file
enc_text = ""
for i in np.transpose(chr_arr):
    for e in i:
        enc_text += e
with open('output_aff.txt', 'w') as file:
    file.write(enc_text)
print("result of encoded text: ", enc_text)

####Decoding####

# input our text in file and correct it a little
with open('output_aff.txt', 'r') as file:
    sentence = file.read().replace(' ', '').upper().replace('\n', '')
print(sentence)

# initialize array for input text
input_text = []


# make string look like 2d arr
def ArrTxt2D(txt):
    text = list(txt)
    print("length of text is ", len(text))
    while len(text) % 4 != 0:
        text.append('Z')
    amount = len(text) / 4
    for i in range(int(amount)):
        a = []
        for j in range(4):
            a.append(text[0])
            text = text[1:]
        input_text.append(a)


ArrTxt2D(sentence)
print(input_text)


# translate character to ASCII
def chrToOrd(txt):
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            txt[i][j] = (ord(txt[i][j]) - ord('A')) % 26


chrToOrd(input_text)
print("ASCII code of characters: ")
for i in range(len(input_text)):
    print(input_text[i])

print()

# transpose 2d matrix(rows becomes columns)
transpose_arr = []
for i in np.transpose(input_text):
    transpose_arr.append(list(i))
print("Transposed matrix of chars: ")
for i in range(len(transpose_arr)):
    print(transpose_arr[i])

# initializing A` matrix
A_shtryh = [[0 for x in range(4)] for z in range(4)]

# inverse matrix
A_inverse = np.linalg.inv(keyA)
print("Inverse A matrix: ", A_inverse)

# calculate A` matrix
for x in range(4):
    for z in range(4):
        A_shtryh[x][z] = (round(A_inverse[x][z] * 17877) * 7) % 26
print("A`: ")
for i in A_shtryh:
    print(i)

# multiplying A` matrix on S key for finding S`
inverse = np.array(A_shtryh)
s = np.array(keyS)
s_strych = np.matmul(inverse, s)
s_str_res = []
for i in s_strych:
    s_str_res.append((i % 26) * (-1))
print("S`: ", s_str_res)

# multiply encoded arr on A`
a_shtryh = np.array(A_shtryh)
crypted = np.array(transpose_arr)
res = a_shtryh.dot(crypted)
dec_res = []
for i in res:
    r = []
    for j in i:
        j = j % 26
        r.append(j)
    dec_res.append(r)
print("Mult encoded array on Aq: ")
for i in dec_res:
    print(i)

x = [[0 for i in range(len(dec_res[0]))] for j in range(len(dec_res))]

# adding S to char arr
for i in range(len(dec_res[0])):
    for j in range(len(dec_res)):
        x[j][i] = (dec_res[j][i] + s_str_res[j]) % 26
print("After adding S`: ")
for i in x:
    print(i)


# return from ASCII to chr
def decodeToChr(text):
    r = []
    for i in range(len(text)):
        res = []
        for j in range(len(text[i])):
            res.append(chr(text[i][j] + ord('A')))
        r.append(res)
    return r


dec_chr_arr = decodeToChr(x)
print("In char: ")
for i in range(len(dec_chr_arr)):
    print(dec_chr_arr[i])

res = ""
for i in np.transpose(dec_chr_arr):
    for j in i:
        res += j
print("results", res)
