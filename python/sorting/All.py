from algorithms.sorting.bubblesort import BubbleSort
from graphviz import Digraph, nohtml
import random

# Test bubble sort
def testBubbleSort():
    a = []
    for i in range(100):
        a.append(i)
    random.shuffle(a)
    s = BubbleSort(a)
    s.sort()
    s.print(lambda x: print(x.key))
    g = s.visualize()
    g.view()


testBubbleSort()
