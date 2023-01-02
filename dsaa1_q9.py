# program to reverse a stack
def reverse_stack(stack):
    stack = reversed(stack)
    return list(stack)
stack = [11,12,13,14,15]

print("Original Stack", *stack, sep='\n')
print("Reversed Stack", *reverse_stack(stack), sep='\n')