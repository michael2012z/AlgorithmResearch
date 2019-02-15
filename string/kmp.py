''' Brute-force method as comparasion base. '''

def naiveSearch (s, p):
    i = 0
    j = 0
    result = []
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                result.append(i - j)
                j = 0
        else:
            i -= j - 1
            j = 0
    return result

'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

def makeTableA(p):
    k = 0 # index of prefix, also the length of continuous matching substring
    table = list([None]*len(p))
    table[0] = -1
    for i in range(1, len(p)):
        table[i] = k
        if p[i] == p[k]:
            k += 1
        else:
            k = 0
    return table


def makeTableB(p):
    k = 0 # index of prefix, also the length of continuous matching substring
    table = list([None]*len(p))
    table[0] = -1
    for i in range(1, len(p)):
        if p[i] == p[k]:
            table[i] = table[k]
            k += 1
        else:
            table[i] = k
            k = 0
    return table

def kmpSearch(s, p):
    '''
    s -> string
    p -> pattern
    '''
    t = makeTableB(p)
    i = 0
    j = 0
    result = []
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                result.append(i - j)
                j = 0
        else:
            i -= t[j]
            j = 0
    return result

'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
''' Test '''

def testNaiveSearch(s, p):
    print(naiveSearch(s, p))    

def testMakeTable():
    p = "abcabdabcaaa"
    table = makeTableB(p)
    print(p)
    print(table)

def testKmpSearch(s, p):
    print(kmpSearch(s, p))    

if __name__ == "__main__":
    ruler = '0         1         2         3         4         5         6         7         8         '
    ruler = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
    s     = 'abcffsbcxfsabcabcabdabcabdaaaaabcabckfdliurewovnmxvbnabcabdabcabdndjklsabcabdabdabdfj'
    p     = 'abcabd'
    testNaiveSearch(s, p)
    testKmpSearch(s, p)
