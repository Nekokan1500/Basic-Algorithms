def kmultiply(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = len(str(x))
        k = round(n/2)
        a = int(x/pow(10,k))
        b = int(x % pow(10,k))
        c = int(y/pow(10,k))
        d = int(y % pow(10,k))
        p = a + b
        q = c + d
        ac = kmultiply(a,c)
        bd = kmultiply(b,d)
        pq = kmultiply(p,q)
        adbc = pq - ac - bd
        return int(pow(10,k*2)*ac + pow(10,k)*adbc + bd)

x = int(input("Enter integer 1: "))
y = int(input("Enter integer 2: "))
print(kmultiply(x,y))
