import random as rand

def create_arr(num):
    l = range(100)
    size = num
    return [rand.choice(l) for i in range(size)]

def bubble_sort(arr):
    n = 0

    n += 1
    for i in range(len(arr)):
        n += 1

        for j in range(len(arr) - i):
            if j+1 <= len(arr)-i-1:

                if arr[j] > arr[j+1]:

                    arr[j], arr[j+1] = arr[j+1], arr[j]

                    n += 1

            n += 3
        
        n += 2

    n += 1

    return arr, n

print(bubble_sort(create_arr(1000)))