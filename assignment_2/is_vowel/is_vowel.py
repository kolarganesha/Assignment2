'''2.2 Write a Python function which takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.'''

vowel = ['a','e','i','o','u']
z = lambda x : x in vowel

print(z('A'.lower()))

#2nd approach
def check_vowel(ch):
    if ch in vowel:
        return True
    else:
        return False

print(z('B'.lower()))
