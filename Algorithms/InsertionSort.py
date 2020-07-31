def InsertionSort(arr):

    # iterating through the array
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print('Sorting...')
    for i in range(len(arr)):
        print('%d ' % arr[i], end=' ')


arr = [12, 11, 13, 5, 6, 45, 70]

InsertionSort(arr)
