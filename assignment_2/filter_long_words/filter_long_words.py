'''1.2 Write a function filter_long_words() that takes a list of words and an integer n
and returns the list of words that are longer than n.'''

def filter_long_words(lis,n):
    lis1=[]
    for i in lis:
        if len(i) > n:
            lis1.append(i)
    return lis1



l = ['abc','abcd','ab','python','c','java','javascript','go']
res = filter_long_words(l,3)
print(res)

