
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
        func(self.value)
    
    def preOrder(self, func):
        func(self.value)
    
    def postOrder(self, func):
        func(self.value)
    

if __name__ == '__main__':
    t = BinaryTree(0)
    t.insertLeft(1)
    t.insertLeft(2)
    t.insertRight(3)
    print (t.height())
    t.inOrder(print)
    
