'''3. Implement a function longestWord() that takes a list of words and returns the longest one.'''

def longest_word(lis):
    max=-1
    for i in lis:
        if len(i) > max :
            max = len(i)
            pos=i

    print(pos)

lis = ['abc','abcd','ab','python','c','java','javascript','go']
longest_word(lis)




