import random

a = range(100)
random.shuffle(a)

def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a

print 'To sort: '
print a
a = BubbleSort(a)
print 'Sorted: '
print a
