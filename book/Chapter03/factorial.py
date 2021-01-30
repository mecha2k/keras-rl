import time

def factorial (x):
    if x == 0:
        return 1
    else:
        return x * factorial (x-1)

time_start = time.clock()
print("Factorial of 10 is: ",factorial (10))
print("Computational time is: ",time.clock() - time_start)
