Empty = input()
S = [int(i) for i in input().split()]


def revers(S):
    res = list()
    for i in range(len(S)):
        res.append(S[len(S) - i - 1])
    return res


def row(S, res):
    result = 0
    flag = False
    for j in range(len(S)):
        for i in range(0, int((len(S) - 1 - j) / 2) + 1):
            flag = True
            if S[i + j] != S[len(S) - 1 - i]:
                flag = False
                break
        if flag == True:
            result = j
            break
        res = revers(S[0:j + 1])
    return result, res


result = list()
cnt, result = row(S, result)
print(cnt)
for i in result:
    print(i, end=" ")
