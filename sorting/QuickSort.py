import random

a = range(1000)
random.shuffle(a)

def QuickSort(a):
    return _QuickSort2(a, 0, len(a)-1)

def _QuickSort1(a, left, right):
#    print a, left, right
    if left >= right:
        return a
    pivot = a[left]
    i = left
    j = right
    while i < j:
        while (i < right) and (a[i] <= pivot):
            i += 1
        while (left < j) and (a[j] >= pivot):
            j -= 1
        if (i < j):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
#    print i,j
    a[left] = a[j]
    a[j] = pivot
 #   print a
#    print 
    _QuickSort1(a, left, j-1)
    _QuickSort1(a, j+1, right)
    return a

def _QuickSort2(a, left, right):
    if left >= right:
        return a
    pivot = a[left]
    i = left
    j = right
    while i < j:
        while (i < j) and a[j] > pivot:
            j -= 1
        a[i] = a[j]
        while (i < j) and a[i] < pivot:
            i += 1
        a[j] = a[i]
    a[i] = pivot
    _QuickSort2(a, left, i-1)
    _QuickSort2(a, j+1, right)
    return a
    

print 'To sort: '
print a
a = QuickSort(a)
print 'Sorted: '
print a
