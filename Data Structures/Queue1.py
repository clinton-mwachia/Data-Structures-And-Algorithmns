'''
USING COLLECTIONS IS MUCH FASTER AS IT OFFERS O(1) 
TIME COMPLEXITY
'''

from collections import deque

q = deque()

# adding elements to the queue
q.append('a')
q.append('b')
q.append('c')

print('Initial queue')
print(q)

print('Elements dequeued from the queue')
print(q.popleft())
print(q.popleft())
print(q.popleft())
