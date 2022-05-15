def len(a):
    j=0
    for i in a:
        j=j+1
    return j

def binsearch(arr,x):
    n=len(arr)
    h=n-1
    l=0
    c=0
    m=(h+l)/2
    for i in a:
        if(x==i):
           c=c+1
        elif (x<i):
            h=m+1
        elif(x>i):
            l=m-1
        else:
            c=0
    return c
    
    

a=[1,2,3,4,5]

x=int(input('enter x to be searched'))
if(binsearch(a,x)==1):
    print('number found')
else:
    print('no number found')
