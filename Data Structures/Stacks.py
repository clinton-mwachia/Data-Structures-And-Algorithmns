# stacks using lists
'''
LIST PROCESS IS SLOW
STACKS INVOLVE PUSHING AND POPPING FROM THE STACK
LISTS PROVIDE A POP AND APPEND O(n) TIME COMPLEXITY
'''
stack = []

# pushing into the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)

# popping elements from the stack
# Last In first out (LIFO)
print('\nElements poped from stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Stack after popping elements')
print(stack)
