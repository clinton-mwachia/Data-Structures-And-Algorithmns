'''
     (1)-- Root Node
    /   \
   /     \  
(2)L.C   (3)Right Child

'''
from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)

# binary tree
print('Binary Tree: ', root)

# list of nodes
print('List of nodes : ', list(root))

# inorder of nodes
print('Inorder of nodes: ', root.inorder)

# tree properties
print('Size of tree: ', root.size)
print('Height of tree: ', root.height)
print('Tree Complete? : ', root.is_complete)
print('Tree Perfect? : ', root.is_perfect)
print('Tree Balanced? : ', root.is_balanced)
