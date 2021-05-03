def stepin(x, d, n):
    d2 = []
    while d!=0:
        d2.append(d%2)
        d = d//2
    d2.reverse()
    z = 1
    for k in range(len(d2)):
        z = z*z
        if d2[k] == 1:
            z = z*x
        z = z%n
    return z

def evkld(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    r = r1%r2
    while r!=0:
        q = r1//r2
        s = s1 - q * s2
        t = t1 - q * t2
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
        r = r1 % r2
    r = r2
    s = s2
    t = t2
    return r, s, t

mod = 26

p = int(input("Input p: "))
q = int(input("Input q: "))

n = p*q
fi =(p - 1) * (q - 1)
print("fi = ", fi)

e = int(input("Input key e: "))

nsd, ss, d = evkld(fi, e)
while nsd != 1:
    e = int(input("Input another key e: "))
    nsd, ss, d = evkld(fi, e)


with open("/Users/workplace/Desktop/before.txt", "r") as f:
    for line in f:
        message = list(line)
f.close()


a, b, g = list(message)
print("first character: ",a)
print("second character: ", b)
print("third character: ", g)


a1 = (ord(a) - ord("A"))
print("first char in ascii representation: ", a1)
b1 = (ord(b)  - ord("A"))
print("second char in ascii representation: ", b1)
g1 = (ord(g)  - ord("A"))
print("third char in ascii representation: ", g1)


c1 = stepin(a1, e, n)
c2 = stepin(b1, e, n)
c3= stepin(g1, e, n)
print("encrypted ascii code first character = ", c1)
print("encrypted ascii code second character = ", c2)
print("encrypted ascii code third character = ", c3)



a1_1 = chr(c1+ ord("A"))
print("transfer encrypted ascii to first character: ", a1_1)
b1_1 = chr(c2+ ord("A"))
print("transfer encrypted ascii to second character: ", b1_1)
c1_1 = chr(c3+ ord("A"))
print("transfer encrypted ascii to third character:",c1_1)


i =[a1_1, b1_1, c1_1]


res = ""
for x in i:
    res += x


f_res = open("/Users/workplace/Desktop/after.txt", "w")
f_res.write(res)
f_res.close()
print("encrypted text = ", res)


with open("/Users/workplace/Desktop/after.txt", "r") as f:
    for a in f:
        encrypted = list(a)
f.close()


e, f, g = list(encrypted)
print("first encrypted character: ",e)
print("second encrypted character: ", f)
print("third encrypted character: ", g)


a1 = (ord(e) - ord("A")) 
print("first encrypted char in ascii representation: ", a1)
b1 = (ord(f)  - ord("A"))
print("second encrypted char in ascii representation: ", b1)
g1 = (ord(g)  - ord("A"))
print("third encrypted char in ascii representation: ", g1)


if d<0:
   d = d + fi
print("key d = ", d)


c1 = stepin(a1, d, n)
c2 = stepin(b1, d, n)
c3= stepin(g1, d, n)
print("decrypted ascii code first character = ", c1)
print("decrypted ascii code fsecond character = ", c2)
print("decrypted ascii code third character = ", c3)



a1_1 = chr(c1+ ord("A"))
print("first decrypted letter: ", a1_1)
b1_1 = chr(c2+ ord("A"))
print("second decrypted letter: ", b1_1)
c1_1 = chr(c3+ ord("A"))
print("third decrypted letter: ",c1_1)


j = [a1_1, b1_1, c1_1]


res = ""
for x in j:
    res += x
print("result: ", res)
