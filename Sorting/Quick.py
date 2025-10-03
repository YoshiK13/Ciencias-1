import random

array=[random.randint(0,100) for i in range(1000)]

n = 0

def quicksort(arr):
    global n

    if(len(arr)>1):       
        piv=int(len(arr)/2)
        val=arr[piv]
        n += 6

        left=[i for i in arr if i<val]
        n += len(arr)

        mid=[i for i in arr if i==val]
        n += len(arr)

        right=[i for i in arr if i>val]
        n += len(arr)

        res=quicksort(left) + mid + quicksort(right)
        n += 4
        return res
    else:
        n += 1
        return arr
        
print(quicksort(array), n)