def add(a,b):
    return a+b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def pow(a,b):
    return a**b
def calc(a,b,c):
    if c=='+':
        return add(a,b)
    elif c=='-':
        return sub(a,b)
    elif c=='*':
        return mul(a,b)
    elif c=='/':
        return div(a,b)
    elif c=='**':
        return pow(a,b)
    else:
        return 'error operation'


x,y,z=eval(input('enter first number\n')),input('enter operation from (+,-,*,**,/,//)\n'),eval(input('enter second number\n'))
print("your result are given below")
print(x , y , z , " = ", calc(x,z,y))