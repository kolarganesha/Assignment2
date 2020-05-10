'''def myfilter(fun,seq):
    m = []
    for i in seq:
        if fun(i):
            m.append(i)
    return m'''

def myfilter(fun,seq):
    for i in seq:
        if fun(i):
            yield i

def odd_even(num):
    if(num%2==0):
        return True
    else:
        return False

lis=[1,2,3,4,8,12,7]
for i in myfilter(odd_even,lis):
    print(i)



