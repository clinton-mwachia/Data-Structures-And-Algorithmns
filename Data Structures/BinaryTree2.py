from binarytree import tree

root = tree()
print('Binary tree of default height(3): ')
print(root)

root2 = tree(height=2)
print('Binary tree of height(2): ')
print(root2)

root3 = tree(height=4, is_perfect=True)
print('Binary tree of height(4) and perfect: ')
print(root3)
