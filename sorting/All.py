import random

class Sortee:
    ''' A key-value pair. '''
    def __init__ (self, key, value):
        self.key = key
        self.value = value

    def __eq__ (self, other):
        return self.key == other.key

    def __ne__ (self, other):
        return self.key != other.key
    
    def __ge__ (self, other):
        return self.key >= other.key

    def __gt__ (self, other):
        return self.key > other.key

    def __le__ (self, other):
        return self.key <= other.key

    def __lt__ (self, other):
        return self.key < other.key

    def __repr__ (self):
        return "(" + str(self.key) + " , " + str(self.value) + ")"

    def __str__ (self):
        return self.__repr__()

    
class Sorter:
    ''' Interface. '''
    def __init__(self, lst):
        self.lst = []
        for i in lst:
            self.lst.append(Sortee(i, i))
        
    def sort(self, ascend = True):
        ''' Nothing is done. '''
        print("Default sort function of sorter, nothing is done.")
        return

    def add(self, sortee):
        self.lst.append(sortee)

    def print(self, printFunction = None):
        ''' Pass sortee to printFunction() '''
        for i in self.lst:
            if printFunction == None:
                print(i)
            else:
                printFunction(i)

                
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
                    
a = []
for i in range(100):
    a.append(i)
random.shuffle(a)
s = BubbleSort(a)
s.sort()
s.print(lambda x: print(x.key))

