from binarytree import bst

root = bst(height=3, is_perfect=False)
print('BST of default height: ', root)

root2 = bst(height=5, is_perfect=True)
print('BST of height 5 and perfect: ', root2)
