print('prime number program')

n = int(input('enter n'))




for i in range(n):
    for j in range(i//2):
        if(n&j==0):
            print('it is not a prime number')
            break
        else:
            print('it is a prime number')