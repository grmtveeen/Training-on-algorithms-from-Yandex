S = list()
flag = (int(input()))
while flag != (-2000000000):
    S.append(flag)
    flag = (int(input()))


def type(S):
    Higher = False
    Smaller = False
    Equel = False
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            Equel = True
        elif S[i] < S[i + 1]:
            Higher = True
        elif S[i] > S[i + 1]:
            Smaller = True
    if (Equel == True) and (Higher != True) and (Smaller != True):
        return "CONSTANT"
    elif (Equel == True) and (Smaller == True) and (Higher != True):
        return "WEAKLY DESCENDING"
    elif (Equel != True) and (Smaller == True) and (Higher != True):
        return "DESCENDING"
    elif (Equel == True) and (Higher == True) and (Smaller != True):
        return "WEAKLY ASCENDING"
    elif (Equel != True) and (Higher == True) and (Smaller != True):
        return "ASCENDING"
    else:
        return "RANDOM"


print(type(S))
