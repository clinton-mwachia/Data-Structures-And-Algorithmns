set1 = set(['a', 'b', 'c'])
print(set1)

# insert data
set1.add('d')

for i in range(1, 6):
    set1.add(i)
print(set1)

# set union
people = {'Jay', 'Idrish', 'Archil'}
vampires = {'Karan', 'Arjun'}
dracula = {'Deepanshu', 'Raju'}

population = people.union(vampires)
print('people union vampires', population)
# or
print('people | vampires', people | vampires)

# INTERSECTION
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

# intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using
# "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)

# DIFFERENCE
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

# Difference of two sets
# using difference() function
print('set1 {}'.format(set1))
print('set2 {}'.format(set2))

set3 = set1.difference(set2)

print("set1.difference(set2):")
print(set3)

# Difference of two sets
set3 = set1 - set2

print("\nset1 - set2::")
print(set3)
