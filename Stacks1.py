'''
IMPLEMENTING STACKS USING COLLECTIONS.DEQUE PYTHON MODULE
IT IS FASTER THAN THE LIST METHOD.
COLLECTIONS PROVIDE O(1) TIME COMPLEXITY
'''
from collections import deque

stack = deque()

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
