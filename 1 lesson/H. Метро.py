a = int(input())
b = int(input())
n = int(input())
m = int(input())

TmaxA = a * (n + 1) + n
TminA = a * (n - 1) + n

TmaxB = b * (m + 1) + m
TminB = b * (m - 1) + m

result = list()
if (TmaxB < TminA) | (TmaxA < TminB):
    print(-1)
else:
    if TminA > TminB:
        result.append(TminA)
    else:
        result.append(TminB)

    if TmaxA < TmaxB:
        result.append(TmaxA)
    else:
        result.append(TmaxB)

    print(int(result[0]), int(result[1]))
