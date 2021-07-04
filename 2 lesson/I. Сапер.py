N, M, K = map(int, input().split())
MASS0 = list()
MASS1 = list()
MASS2 = list()

for i in range(K):
    p, q = map(int, input().split())
    MASS0.append([p, q])

for i in range(N):
    MASS1.append([])
    MASS2.append([])
    for j in range(M):
        MASS1[i].append(0)
        MASS2[i].append(0)

if MASS0 != None:
    for i in range(K):
        MASS1[MASS0[i][0] - 1][MASS0[i][1] - 1] = str(1)


# print(MASS1)

def sum(MASS1, n1, n2, m1, m2):
    result = 0
    for ii in range(n1, n2 + 1):
        for jj in range(m1, m2 + 1):
            result = result + int(MASS1[i + ii][j + jj])
    return result


for i in range(N):
    for j in range(M):

        if i >= 1:
            n1 = -1
        else:
            n1 = 0

        if (i <= (N - 2)):
            n2 = 1
        else:
            n2 = 0

        if (j >= 1):
            m1 = -1
        else:
            m1 = 0

        if (j <= (M - 2)):
            m2 = 1
        else:
            m2 = 0

        MASS2[i][j] = sum(MASS1, n1, n2, m1, m2)

for i in range(K):
    MASS2[MASS0[i][0] - 1][MASS0[i][1] - 1] = "*"

for i in range(N):
    for elem in MASS2[i]:
        print(elem, end=' ')
    print("")
