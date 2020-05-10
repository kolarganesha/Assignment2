'''2.1 Write a Python program using function concept that maps list of words
into a list of integers representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function
output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.'''

l = ['ab', 'cde', 'erty']

'''def len_cal(a):
    z=[]
    for i in a:
        z.append(len(i))
    return z'''

def len_cal1(a):
    for i in a:
       yield len(i)

for i in len_cal1(l):
    print(i)


'''res = len_cal(l)
print(res)'''

# 2nd approach
print(list(map(lambda x : len(x) ,l)))

