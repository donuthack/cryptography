def stepin (x, d, n):
    d2 = []
    while(d!=0):
        d2.append(d%2)
        d = d//2
    d2.reverse()
    z = 1
    for k in range(len(d2)):
        z=z**2
        if d2[k] == 1:
            z=z*x
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
        t = t1 - 1 * t2
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

p = int(input("Input p: "))
q = int(input("Input q: "))

n = p*q
el = (p - 1) * (q - 1)
print("el = ", el)

e = int(input("Input key e: "))

nsd, ss, d = evkld(el, e)
while nsd != 1:
    e = int(input("Input another key e: "))
    nsd, ss, d = evkld(el, e)

m = int(input("Input m: "))

c = stepin(m, e, n)
print("c = ", c)

if d<0:
    d = d + el

m = stepin(c, d, n)
print("m: ", m)
