'''def add(a,b):
    return a+b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def pow(a,b):
    return a**b
    
    
a,c,b=int(input('enter first number\n')),input('enter operation from (+,-,*,**,/,//)\n'),int(input('enter second number'))

if(c=='+'):
    print(add(a,b))
elif(c=='-'):
    print(sub(a,b))
elif(c=='*'):
    print(mul(a,b))
elif(c=='/'):
    print(div(a,b))
elif(c=='**'):
    print(pow(a,b))
else:
    print('wrong operation performed')
    '''


arr=[1,2,3]
arr.pop()
arr.insert(1,5)
print(arr)
arr.append(4)
print(arr)