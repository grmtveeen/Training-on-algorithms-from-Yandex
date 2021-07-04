import math


def func(N, K, M):
    Z = math.floor((N / K))
    if Z == 0:
        return 0, N
    else:
        P = math.floor(K / M)
        if P == 0:
            return 0, N
        else:
            result = P * Z
            Nost = N - P * Z * M
    return result, Nost


N, K, M = map(float, input().split())

P = 0
Pp, Nost = func(N, K, M)
while Pp != 0:
    P = P + Pp
    Pp, Nost = func(Nost, K, M)

print(P)
