def len(a):
    j=0
    for i in a:
        j=j+1
    return j
def sort(a,n):
    min=0
    for i in range(n):
        min=i
        for j in range(i):
            if(a[j]>a[min]):
                min=j
                if(min!=i):
                    tem=a[i]
                    a[i]=a[min]
                    a[min]=tem
               
           
    
    return a
                       
        
    
    
    
    
 
    



a=[1,43,43523,1,-32,143,0]
print(sort(a,len(a)))
