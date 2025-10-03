import random as rand

def create_arr(num):
    l = range(100)
    size = num
    return [rand.choice(l) for i in range(size)]



def seletion_sort(arr):
    n = 0

    for i in range(len(arr)):
        n += 1
        min_i = i
        for j in range(i + 1, len(arr)):
            n += 1
            if arr[j] < arr[min_i]:
                n += 1
                min_i = j

        n += 1
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr, n


print(seletion_sort(create_arr(1000)))