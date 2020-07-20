from heapq import heappop, heappush, heapify

heap = []
heapify(heap)

# using - to sort them
heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20000)
heappush(heap, -1 * 400)

print("Head value of heap : "+str(-1 * heap[0]))

print("The heap elements : ")
for i in heap:
    print(-1 * i, end=' ')
print("\n")
