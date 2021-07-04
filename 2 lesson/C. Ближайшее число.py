Empty = input()
S = [int(i) for i in input().split()]
X = int(input())

def minimum(S, X):
    j = 0
    for i in range(1, len(S)):
        if abs(S[i] - X) < abs(S[j] - X): j = i
    return S[j]

print(minimum(S, X))
