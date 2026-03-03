def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,b%a)

print(gcd(75,90))                