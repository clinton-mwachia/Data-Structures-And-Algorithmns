from tabulate import tabulate

item = input('Enter the data to hash: ')

results = [(item, hash(str(item)))]
print(tabulate(results, headers=['Item', 'Hashed Item']))
