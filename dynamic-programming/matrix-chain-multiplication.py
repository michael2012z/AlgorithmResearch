
def mat_mul_recursive(dim, start, end):
    '''
    You have to pay extra attendition to the index.
    '''
    if start == end:
        return 0
    candidates = []
    for k in range(start, end):
        candidate = mat_mul_recursive(dim, start, k) + \
                    mat_mul_recursive(dim, k+1, end) + \
                    dim[start-1]*dim[k]*dim[end]
        candidates.append(candidate)
    return min(candidates)

def mat_mul_bottom_up (dim, start, end):
    result_table = []
    for i in range(end):
        result_table.append([0] * end)
        for j in range(i):
            result_table[i][j] = '-'            
    for distance in range(1, end-start+1):
        for i in range(1, end-distance+1):
            candidates = []
            j = i + distance
            for k in range(i, j):
                candidate = result_table[i-1][k-1] + \
                            result_table[k+1-1][j-1] +\
                            dim[i-1]*dim[k]*dim[j]
                candidates.append(candidate)
            result_table[i-1][j-1] = min(candidates)
        print("table of distance " + str(distance) + ":")
        for line in result_table:
            print(line)

    return result_table[0][end-1]

if __name__ == "__main__":
    # matrix list:
    # Matrix       A1       A2       A3       A4       A5       A6
    # Dimension    30x35    35x15    15x5     5x10     10x20    20x25
    d = [30, 35, 15, 5, 10, 20, 25]
    #mat_mul = mat_mul_recursive
    mat_mul = mat_mul_bottom_up
    x = mat_mul(d, 1, len(d)-1)
    print(x)
    
