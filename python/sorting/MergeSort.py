import random

a = range(1000)
random.shuffle(a)

def mergeArray(a, first, mid, last):
    i = first
    j = mid
    m = mid
    n = last
    temp = [-1] * (last-first)
    k = 0

    while i < m and j < n:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i < m:
        temp[k] = a[i]
        k += 1
        i += 1
    while j < n:
        temp[k] = a[j]
        k += 1
        j += 1

    for i in range(last-first):
        a[first+i] = temp[i]
        
def _MergeSort(a, first, last):
    if first < last:
        mid = (first + last)/2
        if mid < last:
            _MergeSort(a, first, mid)
        if mid > first:
            _MergeSort(a, mid, last)
        mergeArray(a, first, mid, last)

def MergeSort(a):
    _MergeSort(a, 0, len(a))
    return a

print 'To sort: '
print a
a = MergeSort(a)
print 'Sorted: '
print a
