a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a * d - c * b
det1 = e * d - b * f
det2 = a * f - c * e

if det != 0:
    print(str(2) + ' ' + str(det2 / det) + ' ' + str(det1 / det))
else:
    if (det1 != 0) | (det2 != 0):
        print(0)
    else:
        if ((a != 0) & (b != 0)) | ((c != 0) & (d != 0)):
            if (a == 0) & (b == 0) & (e == 0):
                print(str(1) + " " + str(-c / d) + " " + str(f / d))
            elif (c == 0) & (d == 0) & (f == 0):
                print(str(1) + " " + str(-a / b) + " " + str(e / b))
            elif (b != 0) & (d != 0) & (a != 0) & (c != 0):
                print(str(1) + " " + str(-a / b) + " " + str(e / b))
            else:
                print(str(0))

        elif ((a != 0) & (b == 0)) | ((c != 0) & (d == 0)):
            if (a == 0) & (b == 0) & (e == 0):
                print(str(3) + " " + str(f / c))
            elif (c == 0) & (d == 0) & (f == 0):
                print(str(3) + " " + str(e / a))
            elif (b == 0) & (d == 0) & (a != 0) & (c != 0):
                print(str(3) + " " + str(e / a))
            else:
                print(str(0))

        elif ((a == 0) & (b != 0)) | ((c == 0) & (d != 0)):
            if (a == 0) & (b == 0) & (e == 0):
                print(str(4) + " " + str(f / d))
            elif (c == 0) & (d == 0) & (f == 0):
                print(str(4) + " " + str(e / b))
            elif (b != 0) & (d != 0) & (a == 0) & (c == 0):
                print(str(4) + " " + str(e / b))
            else:
                print(str(0))
