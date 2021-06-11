import random
from graphviz import Digraph, nohtml
import uuid

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
            if type(i) is Sortee:
                self.lst.append(Sortee(i.key, i.value))
            else:
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

    def visualize(self, filename='tmp.gv'):
        g = Digraph('g', filename=filename, node_attr={'shape': 'circle', 'height': '.1'})
        priorNodeName = ""
        for i in self.lst:
            nodeName = str(uuid.uuid1())
            g.node(nodeName, nohtml(str(i.key)))
            if priorNodeName != "":
                g.edge(priorNodeName, nodeName)
            priorNodeName = nodeName
        return g

    def _visualize(self, g):
        nodeName = str(uuid.uuid1())
        g.node(nodeName, nohtml('<l> |<n> ' + str(self.value) + '|<r>'))
        if self.leftChild != None:
            leftUUID = self.leftChild._visualize(g)
            g.edge(nodeName + ':l', leftUUID + ':n')
        if self.rightChild != None:
            rightUUID = self.rightChild._visualize(g)
            g.edge(nodeName + ':r', rightUUID + ':n')
        return nodeName

