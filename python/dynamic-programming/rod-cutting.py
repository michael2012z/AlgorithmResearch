
def raw_top_down(p, n):
    ''' 
    Divide the top level problem into sub-problems recursively.
    Sub-problems could be resolved again and again.
    '''
    if n == 0:
        return 0
    r = -1
    candidates = []
    for i in range(n):
        candidates.append(p[i] + raw_top_down(p, n-1-i))
    r = max(candidates)
    return r

def memoized_top_down(p, n):
    '''
    Top-down algorithm. 
    Store the result of sub-problems in a list to avoid duplicated calculation.
    '''
    m = [-1] * (n+1)
    m[0] = 0
    return _memoized_top_down(p, n, m)

def _memoized_top_down(p, n, m):
    if m[n] != -1:
        return m[n]
    r = -1
    candidates = []
    for i in range(n):
        candidates.append(p[i] + raw_top_down(p, n-1-i))
    r = max(candidates)
    m[n] = r
    return r


def bottom_up(p, n):
    '''
    But the optimal solution from 1, 2, 3, ...
    Store the result in list.
    A latter result is based on previous ones.
    '''
    r = [-1] * (n+1)
    r[0] = 0
    for i in range(1, n+1):
        candidates = []
        for j in range (i):
            candidates.append(p[j] + r[i-1-j])
        r[i] = max(candidates)
    return r[-1]

def bottom_up_with_solution(p, n):
    '''
    Bottom-up algorithm, and tell how to divide.
    When calculating the optimal result of a sub-problem, 
    recored how to divide in that level.
    '''
    r, s = extended_bottom_up_with_solution(p, n)
    solution = []
    while n > 0:
        solution.append(s[n-1])
        n = n - s[n-1]
    print("solution: " + str(solution))
    return r[-1]

def extended_bottom_up_with_solution(p, n):
    r = [-1] * (n+1)
    r[0] = 0
    s = [-1] * (n+1)    
    for i in range(1, n+1):
        q = -1
        candidates = []
        for j in range (i):
            tmp = p[j] + r[i-1-j]
            if q < tmp:
                q = tmp
                s[i] = j+1
        r[i] = q
    return r[1:], s[1:]

if __name__ == "__main__":
    # price list
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(p)
#    func = raw_top_down
#    func = memoized_top_down
#    func = bottom_up
    func = bottom_up_with_solution
    for i in range(1, n+1):
        max_r = func(p, i)
        print("n = " + str(i) + ", max revenue of  = " + str(max_r))
