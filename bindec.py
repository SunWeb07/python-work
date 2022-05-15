def bintodec(bin):
    sum=0
    i=1
    while bin!=0:
        r=bin%10
        sum=sum+r*i
        bin=bin//10
        i=i*2
    return sum



b=1111
print(bintodec(b))


def dectobin(dec):
    sum=0
    i=1
    while dec!=0:
        r=dec%2
        sum=sum+r*i
        dec=dec//2
        i=i*10
    return sum

d=15
print(dectobin(d))
