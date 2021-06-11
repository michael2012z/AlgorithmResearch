
def lcs_recursive(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    elif x[-1] == y[-1]:
        return lcs_recursive(x[:-1], y[:-1]) + 1
    else: # xi != yj
        return max(lcs_recursive(x, y[:-1]), lcs_recursive(x[:-1], y))

def lcs_bottom_up(x, y):
    x = " " + x
    y = " " + y
    table = []
    for i in range(len(x)):
        table.append([(0, "")] * len(y))
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                table[i][j] = ((table[i-1][j-1][0]+1), '\\')
            elif table[i-1][j][0] >= table[i][j-1][0]:
                table[i][j] = (table[i-1][j][0], '-')
            else:
                table[i][j] = (table[i][j-1][0], '|')
    print("===========================")
    for line in table:
        print(line)
    print("===========================")
    # print sequence
    r_seq = ""
    i = len(x)-1
    j = len(y)-1
    while table[i][j][0] > 0:
        if table[i][j][1] == '-':
            i -= 1
        elif table[i][j][1] == '|':
            j -= 1
        else: 
            r_seq += x[i]
            i -= 1
            j -= 1
    seq = []
    for i in range(len(r_seq)-1, 0-1, -1):
        seq.append(r_seq[i])
    print(seq)
    return table[-1][-1][0]
    
if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
#    lcs = lcs_recursive
    lcs = lcs_bottom_up
    s = lcs(X, Y)
    print(s)
    
