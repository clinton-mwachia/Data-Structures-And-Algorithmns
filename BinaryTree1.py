from binarytree import build

nodes = [3, 4, 5, 6, 7, None, 23, 10]

bT = build(nodes)

print('Binary tree from a list: ', bT)

# tree properties
print('Size of tree: ', bT.size)
print('Height of tree: ', bT.height)
print('Tree Complete? : ', bT.is_complete)
print('Tree Perfect? : ', bT.is_perfect)
print('Tree Balanced? : ', bT.is_balanced)
