import random

a = range(100)
random.shuffle(a)

def InsertionSort(a):
    for p in range(1, len(a)):
        tmp = a[p]
        i = p
        while i>0 and tmp<a[i-1]:
            a[i] = a[i-1]
            i -= 1
        a[i] = tmp
    return a

print 'To sort: '
print a
a = InsertionSort(a)
print 'Sorted: '
print a
