from algorithms.basic.stack import Stack

def infixToPostfix(infix):
    infix = infix.split()
    postfix = []
    opStack = Stack()
    opsPri = {'(':0, '*':3, '/':3, '+':4, '-':4}
    highPriOps = ['*', '/']
    lowPriOps = ['*', '/']
    
    for i in infix:
        if i == ')':
            while not opStack.isEmpty():
                topOp = opStack.pop()
                if topOp == '(':
                    break
                else:
                    postfix.append(topOp)
        elif i in ['(', '*', '/', '+', '-']:
            while opStack.isEmpty() == False and opsPri[i] > opsPri[opStack.top()] and opStack.top() != '(':
                postfix.append(opStack.pop())
            opStack.push(i)
        else: # an oprand
            postfix.append(i)

    while not opStack.isEmpty():
        postfix.append(opStack.pop())

    return postfix


if __name__ == '__main__':
    infix = '( A + B ) * C - ( D - E ) * ( F + G )'
    postfix = infixToPostfix(infix)
    print("------ convert infix expression into postfix -------")
    print(infix)
    print(postfix)
    
