A = int(input())
B = int(input())
C = int(input())
E = int(input())
D = int(input())

if ((A <= D) & (B <= E)) | ((A <= E) & (B <= D)) | ((A <= D) & (C <= E)) | ((A <= E) & (C <= D)) | (
        (B <= D) & (C <= E)) | ((B <= E) & (C <= D)):
    print("YES")
else:
    print("NO")
