def equlibrium(a, b, c1, c2, n):
        p1 = (a+c1)/2
        p2 = (a+b*p1+c2)/2

        if n > 0:
            for i in range(n):
                p1 = (a+b*p2+c1)/2
                p2 = (a+b*p1+c2)/2

        return p1, p2


a, b, c1, c2, n = input().split(",")
a = int(a)
b = float(b)
c1 = int(c1)
c2 = int(c2)
n = int(n)

p1Eq, p2Eq = equlibrium(a, b, c1, c2, n)

print("%0.2f %0.2f" % (p1Eq, p2Eq))
