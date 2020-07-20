from queue import Queue

q = Queue(maxsize=5)
print('Size of the queue is :{}'.format(q.qsize()))

# adding elements into the queue
q.put('a')
q.put('b')
q.put('c')

print('full? {}'.format(q.full()))

# removing elements
print(q.get())
print(q.get())
print(q.get())

print('Empty :{}'.format(q.empty()))
