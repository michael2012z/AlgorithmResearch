
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

if __name__ == "__main__":
    p = "abcabdabcaaa"
    table = makeTable(p)
    print(p)
    print(table)
