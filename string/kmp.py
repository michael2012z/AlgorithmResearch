
def makeTable(p):
    k = 0
    c = 0
    table = list([None]*len(p))
    table[0] = -1
    for i in range(1, len(p)):
        if p[i] == p[k]:
            c += 1
            table[i] = table[k]
            k += 1
        else:
            table[i] = c
            c = 0
            k = 0
    return table

if __name__ == "__main__":
    p = "aaabaaa"
    table = makeTable(p)
    print(p)
    print(table)
