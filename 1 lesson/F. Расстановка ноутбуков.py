a, b, c, d = map(int, input().split())

S = list()

if a > c:
    S.append((b + d) * a)
else:
    S.append((b + d) * c)

if b > c:
    S.append((a + d) * b)
else:
    S.append((a + d) * c)

if a > d:
    S.append((b + c) * a)
else:
    S.append((b + c) * d)

if b > d:
    S.append((a + c) * b)
else:
    S.append((a + c) * d)

minI = 0
minS = S[0]

for i in range(4):
    if S[i] < minS:
        minS = S[i]
        minI = i

if minI == 0:
    if a > c:
        print(str(b + d) + ' ' + str(a))
    else:
        print(str(b + d) + ' ' + str(c))

elif minI == 1:
    if b > c:
        print(str(a + d) + ' ' + str(b))
    else:
        print(str(a + d) + ' ' + str(c))

elif minI == 2:
    if a > d:
        print(str(b + c) + ' ' + str(a))
    else:
        print(str(b + c) + ' ' + str(d))

elif minI == 3:
    if b > d:
        print(str(a + c) + ' ' + str(b))
    else:
        print(str(a + c) + ' ' + str(d))
