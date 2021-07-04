S = [int(i) for i in input().split()]

def What_is(S):
    Ground = True
    for i in range(len(S) - 1):
        if S[i] >= S[i + 1]:
            Ground = False
            break
    if Ground: return "YES"
    return "NO"

print(What_is(S))