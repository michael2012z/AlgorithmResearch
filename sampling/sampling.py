import random

def genSamples0(n, m):
    '''
    The possibility that the 0th element was chosen is m/n;
    If element 0 was chosen, the possibility of 1st element was (m-1)/(n-1);
    Otherwise, the possibility of 1st element was m/(n-1);
    ......
    Complexity: O(n)
    '''
    s = []
    for i in range(n):
        if random.randrange(n-i) < m:
          s.append(i)
          m -= 1
    return s

def genSamples1(n, m):
    '''
    Go through the first m elements, exchange each with a random later one, and sort.
    The efficiency of the algorithm is determined by the sorting, 
    so the complexity can't be better than O(nlogn).
    '''
    l = list(range(n))
    for i in range(m):
        j = random.randrange(i, n)
        l[i], l[j] = l[j], l[i]
    return sorted(l[:m])
    
if __name__ == "__main__":
    n = 1000
    m = 100
    print ("Randomly choose", m, "numbers out of", n, ":")
    samples = genSamples0(1000, 100)
    print (samples)

