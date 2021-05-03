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
def decToBin(d):
    d2 = []
    while(d!=0):
        d2.append(d%2)
        d = d//2
    d2.reverse()
    return d2

p = int(input("Input p: "))
q = int(input("Input q: "))

print("Person A: ")
ka = int(input("Input k(a): "))
ya = stepin(q, ka, p)
print("y(a) = ", ya)

print("Person B: ")
kb = int(input("Input k(b): "))
yb = stepin(q, kb, p)
print("y(b) = ", yb)

print("for operator A: ")
Yb = stepin(yb, ka,p)
Yb_a = decToBin(Yb)
print("Y(b) = ", Yb)
print("binary Y(b)_a = ", Yb_a)

print("for person B: ")
Ya = stepin(ya, kb,p)
Ya_b = decToBin(Ya)
print("Y(a) = ", Ya)
print("binary Y(a)_b = ", Ya_b)

message = []
with open("/Users/workplace/Desktop/gamal_text.txt", "r") as f:
    for line in f:
        message.append(int(line.strip("\n")))
f.close()


c_res = ""
for i in range(len(message)):
    message_b = decToBin(message[i])
    print("binary message = ", message_b)

    if len(message_b) <= len(Ya_b):
        ki = len(message_b)
    else:
        ki = len(Ya_b)

    c = []
    for j in range(ki):
        c.append(message_b[j]^Ya_b[j])
        c_res = c_res + str(c[j])

f_res = open("/Users/workplace/Desktop/res_gam.txt", "w")
f_res.write(c_res)
f_res.close()
print("c = ", c)

for i in range(len(c)):
    if len(c) <= len(Yb_a):
        ki = len(c)
    else:
        ki = len(Yb_a)

    message_sh = []
    for j in range(ki):
        message_sh.append(c[j]^Yb_a[j])
print("message for check = ", message_sh)
