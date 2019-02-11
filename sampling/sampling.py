import random

def genSamples0(n, m):
    s = []
    for i in range(n):
        if random.randrange(n-i) < m:
          s.append(i)
          m -= 1
    print (s)


if __name__ == "__main__":
    genSamples0(100, 10)

