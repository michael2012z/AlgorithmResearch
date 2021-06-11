import random

a = range(1000)
random.shuffle(a)

def HeapSort(a):
    # build a heap
    # precolate down methodology
    # from the a/2-th element backward
    for i in range(len(a)/2, -1, -1):
        x = a[i]
        j = i
        while(j < len(a)):
            right = 2*j+2
            left = 2*j+1
            k = j
            if (right < len(a)) and (a[right] > a[left]):
                k = right
            elif (left < len(a)):
                k = left
            if (k <> j) and (a[k] > x):
                a[j] = a[k]
                j = k
            else:
                break
        a[j] = x
    print "heap: "
    print a
    # sort the heap
    for i in range((len(a)-1), 0, -1):
        # swap top and last
        x = a[i]
        a[i] = a[0]
        a[0] = x
        # regulate the heap
        j = 0
        x = a[0]
        while (j < i):
            left = j*2+1
            right = j*2+2
            k = j
            if (right < i) and (a[left] < a[right]):
                k = right
            elif (left < i):
                k = left
            if (k <> j) and (a[k] > x):
                a[j] = a[k]
                j = k
            else:
                break
        a[j] = x
    return a

print 'To sort: '
print a
a = HeapSort(a)
print 'Sorted: '
print a
