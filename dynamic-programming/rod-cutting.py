
def raw_top_down(p, n):
    if n == 0:
        return 0
    r = -1
    candidates = []
    for i in range(n):
        candidates.append(p[i] + raw_top_down(p, n-1-i))
    r = max(candidates)
    return r
    
if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(p)
    for i in range(1, n+1):
        max_r = raw_top_down(p, i)
        print("n = " + str(i) + ", max revenue of  = " + str(max_r))
