

class BinaryHeap:
    '''
    Min Heap
    '''
    
    heapList = []
    heapSize = 0
    
    def __init__ (self):
        pass

    def minChild(self, i):
        l = i * 2 + 1 # left child
        r = l + 1 # right child
        t = 0 # target index, left or right
        if r < self.heapSize: # right child exist, then left child must exist
            if self.heapList[l] < self.heapList[r]:
                t = l
            else:
                t = r
        elif l < self.heapSize: # right child not existing, but left child is
            t = l
        else:
            t = -1

        return t
    
    def goUp(self, i):
        while i > 0:
            p = i // 2 # parent
            if self.heapList[i] < self.heapList[p]:
               self.heapList[i], self.heapList[p] = self.heapList[p], self.heapList[i]
               i = p
            else:
                break

    def goDown(self, i):
        while i < self.heapSize:
            c = self.minChild(i)
            if c == -1:
                break
            else:
                self.heapList[i], self.heapList[c] = self.heapList[c], self.heapList[i]
                i = c



      '''
   0 
 1   2
3 4 5 6 

i-1 // 2 
      '''
      
