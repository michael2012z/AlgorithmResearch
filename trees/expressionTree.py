from algorithms.trees.binaryTree import BinaryTree

def buildExpressionTree(exp):
    return None

if __name__ == "__main__":
    print ("----- buildExpressionTree -----")
    et = buildExpressionTree(' 5 * ( 3 + 4 ) - 3 - ( 9 - 7 ) / 2 ')
    et.inOrder(print)
