import random
x = []
for i in range(10):
    x.append(random.randint(1,100))

def BubbleSort(Arr):
    for i in range(len(Arr)):
        if Arr[i] > Arr[i+1]:
            temp = Arr[i]
            temp2 = Arr[i + 1]
            Arr[i+1] = temp
            Arr[i] = temp2            
            BubbleSort(Arr)
        if Arr[i+1] >= Arr[i]:
            print(Arr)
    return(Arr)
#O(N^2 - N) Has Recursion
#BubbleSort(arrat)

def test(x):
    for i in range(len(x)-1):
        if x[i] == x[len(x)-1]:
            return(x)
        elif x[i] > x[i+1]:
            first = x[i]
            second = x[i+1]
            x[i] = second
            x[i+1] = first
            test(x)
        else:
            pass





def Sort(Array):
    for i in range(0, len(Array)):
       for j in range(0, len(Array)):
            if Array[i] < Array[j]:
                Array[i], Array[j] = Array[j], Array[i]
                print(Array)
            else:
                print(Array)
    return(Array)
#O(N^2)

test(x)

