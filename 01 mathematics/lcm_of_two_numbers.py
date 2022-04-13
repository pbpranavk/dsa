def gcd(a, b):
    if (a==0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b) :
        return gcd (a - b , b)

    return gcd (a  , b -a)

def lcm(a,b):
    return (a / gcd(a,b)) * b

print(lcm(15, 20))