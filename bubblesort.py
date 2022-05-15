def debubblesort(a,n):
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]<a[j+1]):
                tem=a[j]
                a[j]=a[j+1]
                a[j+1]=tem
               
           
    
    return a

def asbubblesort(a,n):
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tem=a[j]
                a[j]=a[j+1]
                a[j+1]=tem
               
           
    
    return a



def len(a):
    j=0
    for i in a:
        j=j+1
    return j
a=[1,3,1]
print(debubblesort(a,len(a)))

