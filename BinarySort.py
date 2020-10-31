def binarySort(array, product):
    mid = len(array) // 2
    L = array[:mid]
    R = array[mid:]
    if product > array[mid]:
        print("Greater Than")
        binarySort(R, product)
    elif product < array[mid]:
        print("Less Than")
        binarySort(L, product)
    else:
        print(array[mid])



arr = [1,3,6,8,19,21,41,53,75]

binarySort(arr, 1)