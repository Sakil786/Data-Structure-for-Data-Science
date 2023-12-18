"""Problem: Given two arrays ,write a function to get the intersection of the two:For example,if
A=[1,2,3,4,5] and B=[0,1,3,7] then you should return [1,3]"""


def intersection(a, b):
    set_a = set(a)
    set_b = set(b)
    if len(set_a) < len(set_b):
        y = [x for x in set_a if x in set_b]
        return y
    else:
        x = [x for x in set_b if x in set_a]
        return x
a = [1, 2, 3, 4, 5]
b = [0, 1, 3, 7]
y = intersection(a, b)
print(y)
