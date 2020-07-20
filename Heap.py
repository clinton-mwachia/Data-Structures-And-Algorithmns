'''
IN MAX HEAP, THE PARENT NODE HAS THE HIGHEST VALUE AND 
DECREASES AS YOU GO DOWN THE BINARY TREE
'''

from binarytree import heap

root = heap(height=3, is_max=True, is_perfect=False)
print('Max-heap of height 3', root)


root2 = heap(height=3, is_max=False, is_perfect=True)
print('Min-heap of height 3', root2)

root3 = heap()