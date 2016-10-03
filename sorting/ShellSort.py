import random

a = range(1000)
random.shuffle(a)

def ShellSort(a):
    interval = len(a)/2
    while interval > 0:    
        for p in range(interval, len(a)):
            tmp = a[p]
            i = p
            while i>0 and tmp<a[i-interval]:
                a[i] = a[i-interval]
                i -= interval
            a[i] = tmp
        interval /= 2
    return a

print 'To sort: '
print a
a = ShellSort(a)
print 'Sorted: '
print a
