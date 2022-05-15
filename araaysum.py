import array
ar=array.array('i',[1,2,3,4,5])

sum=0

for i in ar:
    sum+=i

print(sum)



def student( name, roll ):
    print(name,roll)
student("George",98)
def student(name,roll,mark):
    print(name,roll,mark)
student(90,102,"bala")
def student( name, age=17):
    print (name, age)
student( "kumar\t")
student( "ajay",89)
def student( name,*mark):
    print(name,mark)
student ("bala",102,90)

a=50
def addg():
    b=20
    
    return a+b 
def suml():
    b=20
    a=30
    return a+b
   
   
   
print(suml(),addg())

'''

1. Sum of array of elements.
2. Demonstrate function parameters or arguments (4 types).
3. Demonstrate local and global scope of a variable with the help of .functions
4. Demonstrate call one function within another function
5. Perform recursive factorial.
6. Extract substring from a given string
7. Perform GCD of 2 numbers.'''


def wave():
    return "hello"
    
def greet(wave):
    return wave+", good morning."

    
greey=greet(wave())
print(greey)

def gcd( x, y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
    
print(gcd(8,2))


name=["sunny","praveen","aaquib","ibrahim","yasser","abdulla"]
print(name[0:4:1])
print(name[0:])
print(name[:5])
def recursive(n):
    if(n==0):
        return 1
    else: return recursive(n-1)*n
    
print(recursive(5))

square=lambda x:x*x
print(square(5))