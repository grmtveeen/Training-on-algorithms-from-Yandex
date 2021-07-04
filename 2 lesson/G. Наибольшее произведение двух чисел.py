S = [int(i) for i in input().split()]


def dop(X, X1, X2, TF1, TF2):
    if TF1 == False:
        X1 = X
        TF1 = True
    elif TF2 == False:
        if X1 <= X:
            X2 = X1
            X1 = X
        else:
            X2 = X
        TF2 = True
    elif X1 <= X:
        X2 = X1
        X1 = X
    elif X2 <= X:
        X2 = X
    return X1, X2, TF1, TF2


def func(S):
    MaxA = False
    MaxA2 = False
    MaxB = False
    MaxB2 = False
    A = 0
    A2 = 0
    B = 0
    B2 = 0
    for i in range(len(S)):
        if S[i] > 0:
            A, A2, MaxA, MaxA2 = dop(S[i], A, A2, MaxA, MaxA2)
        elif S[i] < 0:
            B, B2, MaxB, MaxB2 = dop(abs(S[i]), abs(B), abs(B2), MaxB, MaxB2)
            B = -B
            B2 = -B2
    if ((MaxA == True) and (MaxA2 == True)) or ((MaxB == True) and (MaxB2 == True)):
        if (A * A2 > B * B2):
            return A2, A
        else:
            return B, B2
    else:
        if (S[0] <= S[1]):
            return S[0], S[1]
        else:
            return S[1], S[0]


S1, S2 = func(S)
print(S1, S2)
