'''
queue module makes use of the put and get methods
'''
from queue import LifoQueue

stack = LifoQueue(maxsize=4)

print(stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')
stack.put('e')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())
