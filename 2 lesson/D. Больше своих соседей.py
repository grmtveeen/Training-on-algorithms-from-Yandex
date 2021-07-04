S = [int(i) for i in input().split()]


def how_much(S):
    j = 0
    for i in range(1, len(S) - 1):
        if (S[i - 1] < S[i]) and (S[i] > S[i + 1]): j = j + 1
    return j


print(how_much(S))
