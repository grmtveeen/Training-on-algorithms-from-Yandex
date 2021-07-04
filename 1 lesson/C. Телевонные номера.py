def func(s):
    number = list()
    result = list()
    for i in range(len(s)):
        if (s[i] != "-") & (s[i] != ")") & (s[i] != "(") & (s[i] != "+"): number.append(s[i])

    if len(number) == 7:
        result[0:2] = ['4', '9', '5']
        result[3:9] = number
    else:
        result = number[1:11]
    return result


s = [input() for i in range(4)]
numbers = [func(s[i]) for i in range(4)]

YN = False
for i in range(1,4):
    if numbers[0] == numbers[i]:
        print("YES")
    else:
        print("NO")
