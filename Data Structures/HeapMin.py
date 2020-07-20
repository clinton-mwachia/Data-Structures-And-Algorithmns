from heapq import heappop, heappush, heapify

heap = []
heapify(heap)

# using - to sort them
heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 2000)
heappush(heap, 400)

print("Head value of heap : "+str(heap[0]))

print("The heap elements : ")
for i in heap:
    print(i, end=' ')
print("\n")

element = heappop(heap)

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end=' ')
