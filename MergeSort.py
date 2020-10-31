import random

def randomDataGen(amount):
    list1 = []
    for i in range(amount):
        n = random.randint(1,10000000)
        list1.append(n)
    return list1

def mergeSort(values):
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left = mergeSort(values[:mid])
    right = mergeSort(values[mid:])
    sort = []
    LIndex = 0
    RIndex = 0
    while LIndex < len(left) and RIndex < len(right):
        if left[LIndex] < right[RIndex]:
            sort.append(left[LIndex])
            LIndex += 1
        else:
            sort.append(right[RIndex])
            RIndex += 1
    sort += left[LIndex:]
    sort += right[RIndex:]
    return sort
    

n = randomDataGen(1000000)
print(mergeSort(n))    



  