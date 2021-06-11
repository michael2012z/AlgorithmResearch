import sys
sys.path.append('../stack')
from algorithms.basic.stack import Stack
from algorithms.trees.binaryTree import BinaryTree
from expression import infixToPostfix

def makeTree(stack):
    i = stack.pop()
    t = BinaryTree(i)    
    if i in ['+', '-', '*', '/']:
        if not stack.isEmpty():
            rightTree = makeTree(stack)
            t.insertRight(rightTree)
        if not stack.isEmpty():
            leftTree = makeTree(stack)
            t.insertLeft(leftTree)
    return t

def postfixToTree(postfix):
    stack = Stack(postfix)
    tree = None
    if not stack.isEmpty():
        tree = makeTree(stack)
    return tree

if __name__ == "__main__":
    print ("----- buildExpressionTree -----")

    infix = '( A + B ) * C - ( D - E ) * ( F + G )'
    print ("infix expression:")
    print (infix)

    postfix = infixToPostfix(infix)
    print ("postfix expression:")
    print (''.join(postfix))

    et = postfixToTree(postfix)
    e = []
    et.inOrder(e.append)
    print ("expression tree:")
    print(''.join(e))
