import selectsort as p


def getdata(arr):
    
    i=int(input('enter no. of elements'))

    for k in range(i):
        k=int(input('enter elements'))
        arr.append(k)
        
    return arr 
loc=[]
getdata(loc)

print(p.deselectsort(loc,p.len(loc)))