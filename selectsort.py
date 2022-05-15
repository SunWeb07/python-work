def len(at):
    k=0
    for l in at:
        k=k+1
    return k
def asselectsort(ar,n):
    min=0
    for i in range(n):
        min=i
        for j in range(i):
            if(ar[j]>ar[min]):
                min=j
                if(min!=i):
                    tem=ar[i]
                    ar[i]=ar[min]
                    ar[min]=tem
               
           
    
    return ar


def deselectsort(ar,n):
    min=0
    for i in range(n):
        min=i
        for j in range(i):
            if(ar[j]<ar[min]):
                min=j
                if(min!=i):
                    tem=ar[i]
                    ar[i]=ar[min]
                    ar[min]=tem
               
           
    
    return ar
               
        
    
    
    
    
 
    




