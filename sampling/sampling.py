;; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer.

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

