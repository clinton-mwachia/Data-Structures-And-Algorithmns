import array

arr = array.array('i', [1, 2, 3, 4])

print("The created array is : ", end='')

# arrays in python start form 0
for i in range(0, 4):
    print(arr[i], end='')

print('\r')

# appending an item to an array
print('Appending...')
arr.append(45)

for i in range(0, 5):
    print(arr[i], end='')

# inserting at a specified position
arr.insert(1, 0)

print('Inserting at position 1...')
for i in range(0, 5):
    print(arr[i], end='')

print('\r')
# popping an array
print('Popped element is: ', end='')
print(arr.pop(0))
print('\r')
print('printing array after popping...')
for i in range(0, 5):
    print(arr[i], end='')

# index
print ("The index of 1st occurrence of 4 is : ",end="") 
print (arr.index(4))

# using typecode to print datatype of array 
print ("The datatype of array is : ") 
print (arr.typecode) 
  
# using itemsize to print itemsize of array 
print ("The itemsize of array is : ") 
print (arr.itemsize) 
  
# using buffer_info() to print buffer info. of array 
print ("The buffer info. of array is : ") 
print (arr.buffer_info()) 