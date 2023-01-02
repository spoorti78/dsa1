#program to convert postfix to prefix expression.
def is_operator(n):
    if n == "+":
        return True
    if n == "-":
        return True
    if n == "/":
        return True
    if n == "*":
        return True
    return False

def post_pre(x):
    s = []
    length = len(x)
    for i in range(length):
        if (is_operator(x[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = x[i] + op2 + op1
            s.append(temp)
        else:
             s.append(x[i])
    ans = ""
    for i in s:
        ans += i
    return ans

x = input("Enter expression = ")
print("Prefix : ", post_pre(x))