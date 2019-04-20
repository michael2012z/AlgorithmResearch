
def mat_mul_recursive(dim, start, end):
    '''
    You have to pay extra attendition to the index.
    '''
    if start == end:
        return 0
    candidates = []
    for k in range(start, end):
        candidate = mat_mul_recursive(dim, start, k) + mat_mul_recursive(dim, k+1, end) + dim[start-1]*dim[k]*dim[end]
        candidates.append(candidate)
    return min(candidates)


if __name__ == "__main__":
    # matrix list:
    # Matrix       A1       A2       A3       A4       A5       A6
    # Dimension    30x35    35x15    15x5     5x10     10x20    20x25
    d = [30, 35, 15, 5, 10, 20, 25]
    mat_mul = mat_mul_recursive
    x = mat_mul(d, 1, len(d)-1)
    print(x)
    
