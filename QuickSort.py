import random

def randomDataGen(amount):
    list1 = []
    for i in range(amount):
        n = random.randint(1,10000000)
        list1.append(n)
    return list1



def quicksort(lists):
    if len(lists) <= 1:
        return lists
    LPivot = []
    GPivot = []
    piviot = lists[0]
    for i in lists[1:]:
        if i <= piviot:
            LPivot.append(i)
        else:
            GPivot.append(i)
    return(quicksort(LPivot) + [piviot] + quicksort(GPivot))
    

    
    
    
    

numbers = randomDataGen(100)
print(quicksort(numbers))