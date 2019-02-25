
class BinaryHeap:
    '''
    Min Heap
    '''
    
    heapList = []
    heapSize = 0
    
    def __init__ (self, l = []):
        self.heapList = l
        self.heapSize = len(l)
        i = (self.heapSize - 1 - 1) // 2 # last non-leaves node
        while i > -1:
            self.goDown(i)
            i -= 1

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
            p = (i - 1) // 2 # parent
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
            elif self.heapList[i] > self.heapList[c]:
                self.heapList[i], self.heapList[c] = self.heapList[c], self.heapList[i]
                i = c
            else:
                break

    def insert(self, key):
        self.heapList.append(key)
        self.heapSize += 1
        self.goUp(self.heapSize-1)

    def remove(self):
        top = self.heapList[0]
        self.heapList[0] = self.heapList.pop()
        self.heapSize -= 1
        self.goDown(0)
        return top

    def size(self):
        return self.heapSize

    def getList(self):
        return self.heapList

      
if __name__ == '__main__':
    print('+++++++++++ test 1 ++++++++++++++')
    l = [3, 5, 2, 6, 4, 1, 0]
    bh = BinaryHeap(l)
    print(bh.getList())
    print('+++++++++++ test 2 ++++++++++++++')
    l = [0, 1, 2, 3, 4, 5, 6]
    bh = BinaryHeap(l)
    print(bh.getList())
    print('+++++++++++ test 3 ++++++++++++++')
    l = [2, 3, 4, 5, 6, 7, 8]
    bh = BinaryHeap(l)
    bh.insert(9)
    bh.insert(1)
    bh.insert(0)
    bh.remove()
    print(bh.getList())
