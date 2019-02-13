
def makeTable(p):
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
    t = makeTable(p)
    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                return i - j
        else:
            i -= t[j]
            j = 0
    return -1

if __name__ == "__main__":
    p = "abcabdabcaaa"
    table = makeTable(p)
    print(p)
    print(table)
    print("++++++++++++")
    print(kmpSearch("abcabcabdabc", "abcabd"))
    
