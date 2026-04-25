# Find the Factorial of the given number :

# input  5 -- 120

# input 2 -- 2

# input  0 -- 1

# input -8 -- Not defined

n = int(input("Enter the Number :"))

if n < 0:
    print("Not defined")
elif n == 0:
    print(1)
else:
    result = 1
    for i in range(1,n+1):
        result=result*i
    print(result)