import random

a = range(100)
random.shuffle(a)

def HeapSort(a):
    # build a heap
    for i in range(len(a)/2, len(a)):
        j = i
        while(j > 0):
            p = (j-1)/2
            if a[j] > a[p]:
                tmp = a[j]
                a[j] = a[p];
                a[p] = tmp
            j = p
    # sort the heap
    for i in range((len(a)-1), 0, -1):
        # swap top and last
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp
        # regulate the heap
        j = 0
        while (j < i):
            left = j*2+1
            right = j*2+2
            k = j
            if (right < i) and (a[left] < a[right]):
                k = right
            elif (left < i):
                k = left
            if (k <> j) and (a[k] > a[j]):
                tmp = a[k]
                a[k] = a[j]
                a[j] = tmp
                j = k
            else:
                break
    return a

print 'To sort: '
print a
a = HeapSort(a)
print 'Sorted: '
print a
