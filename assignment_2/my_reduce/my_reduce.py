'''1.1 Write a Python Program to implement your own myreduce() function
which works exactly like Python's built-in function reduce()'''

def myreduce(fun,seq):
    res = seq[0]
    for i in seq[1:]:
        res = fun(res,i)
    return res

def mul(x,y):
    return x*y

l = [1,2,3,4]
print("result = ",myreduce(mul,l))
