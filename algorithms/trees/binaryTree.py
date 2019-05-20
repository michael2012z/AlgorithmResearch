from graphviz import Digraph, nohtml
import uuid

class BinaryTree:
    value      = None
    leftChild  = None
    rightChild = None

    def __init__ (self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, node):
        if not isinstance(node, BinaryTree):
            node = BinaryTree(node)

        if self.leftChild is not None:
            node.leftChild = self.leftChild

        self.leftChild = node

    def insertRight(self, node):
        if not isinstance(node, BinaryTree):
            node = BinaryTree(node)

        if self.rightChild is not None:
            node.rightChild = self.rightChild

        self.rightChild = node

    def height(self):
        maxLeft = 0
        maxRight = 0
        if self.leftChild != None:
            maxLeft = self.leftChild.height()
        if self.rightChild != None:
            maxRight = self.rightChild.height()
        return 1 + max(maxLeft, maxRight)

    def inOrder(self, func):
        if self.leftChild != None:
            self.leftChild.inOrder(func)
        func(self.value)
        if self.rightChild != None:
            self.rightChild.inOrder(func)
    
    def preOrder(self, func):
        func(self.value)
        if self.leftChild != None:
            self.leftChild.inOrder(func)
        if self.rightChild != None:
            self.rightChild.inOrder(func)
    
    def postOrder(self, func):
        if self.leftChild != None:
            self.leftChild.inOrder(func)
        if self.rightChild != None:
            self.rightChild.inOrder(func)
        func(self.value)

    def visualize(self, filename='tmp.gv'):
        g = Digraph('g', filename=filename, node_attr={'shape': 'record', 'height': '.1'})
        self._visualize(g)
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

            
if __name__ == '__main__':
    t = BinaryTree(0)
    t.insertLeft(1)
    t.insertLeft(2)
    t.insertRight(3)
    print ("----- height -----")
    print (t.height())
    print ("----- inOrder -----")
    t.inOrder(print)
    print ("----- preOrder -----")
    t.preOrder(print)
    print ("----- postOrder -----")
    t.postOrder(print)
    g = t.visualize()
    g.view()
    
