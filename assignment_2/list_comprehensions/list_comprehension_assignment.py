''' 2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
 [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''

#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

word = "ACADGILD"
r1 = [i for i in word]
print(r1)

#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
l1 = ['x', 'y', 'z']
r2 = [i*j for i in l1 for j in range(1,5)]
print(r2)

#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
l2 = ['x', 'y', 'z']
r3 = [i*j for i in range(1,5) for j in l2]
print(r3)

#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
l3 = [2, 3, 4]
r4 = [[i+j] for i in l3 for j in range(0,3) ]
print(r4)

#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
l3 = [2, 3, 4, 5]
r4 = [[i+j for i in l3] for j in range(0,4) ]
print(r4)

#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
r5 = [(j,i) for i in range(1,4) for j in range(1,4)]
print(r5)