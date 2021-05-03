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

p = int(input("Input p: "))
while p%4 != 3:
    p = int(input("Input p: "))

q = int(input("Input q: "))
while q%4 != 3:
    q = int(input("Input q: "))
M = int(input("Input M: "))

n = p*q

k = (p+1)/4
l = (q+1)/4
print("k = ", k)
print("l = ", l)

nsd, s, t = evkld(q, p)
if s<0:
    s = s+p
elif t<0:
    t = t+q
print("q inverse = ", s)
print("p inverse = ", t)


a = q*s
b = p*t
print("a = ", a)
print("b = ", b)

if n > M :
    C = stepin(M, 2, n)
    print("C = ", C)
    m1 = stepin(C, int((p+1)/4), p)
    m3 = stepin(C, int((q+1)/4), q)
    M1 = (a*m1+b*m3)%n
    M2 = (a*m1-b*m3)%n
    M3 = (a*(-m1)+b*m3)%n
    M4 = (a*(-m1)-b*m3)%n
    print("m1 = ", m1)
    print("m3 = ", m3)
    print("M1 = ", M1)
    print("M2 = ", M2)
    print("M3 = ", M3)
    print("M4 = ", M4)