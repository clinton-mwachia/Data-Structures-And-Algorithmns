'''
IMPLEMENTING QUEUES USING LIST
LIST PROVIDE A TIME COMPLEXITY OF O(n)
'''
queue = []

# adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print('Initial queue')
print(queue)

# removing elements from the queue
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('Queue after removing elements')
print(queue)
