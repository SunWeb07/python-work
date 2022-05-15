arr=[]
for i in range(3):
    a=int(input("enter your value"))
    arr.append(a)

print(arr)
k=int(input("enter the value you want to insert"))
l=len(arr)+1
print(k,arr,l)
arr.append(k)
print(arr)