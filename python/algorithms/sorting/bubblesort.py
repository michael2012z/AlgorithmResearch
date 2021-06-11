from .sort import Sorter
from graphviz import Digraph, nohtml
import uuid
               
class BubbleSort(Sorter):
    def __init__(self, lst):
        super().__init__(lst)

    def sort(self, ascend = True):
        compare = lambda x, y : x > y
        if ascend == False:
            compare = lambda x, y : x < y
            
        for i in range(len(self.lst)-1, 0, -1):
            for j in range(0, i):
                if compare(self.lst[j], self.lst[j+1]):
                    tmp = self.lst[j]
                    self.lst[j] = self.lst[j+1]
                    self.lst[j+1] = tmp

                    
if __name__ == '__main__':
    a = []
    for i in range(100):
        a.append(i)
    random.shuffle(a)
    s = BubbleSort(a)
    s.sort()
    s.print(lambda x: print(x.key))
    g = s.visualize()
    g.view()
    
