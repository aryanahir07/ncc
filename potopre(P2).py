def postfix(a):
    a=a.split()
    stack=[]

    for ele in a:
        if ele not in '/*+-':
            stack.append(int(ele))
        else:
            right= stack.pop()
            left= stack.pop()

            if ele == '+':
                stack.append(left+right)
            elif ele == '-':
                stack.append(left-right)
            elif ele == '*':
                stack.append(left*right)
            elif ele == '/' :
                stack.append(left/right)

    return stack.pop()

a="10 6 9 3 + -11 * / * 17 + 5 +"
answer = postfix(a)
print("Value of given expression is :" + str(answer) )