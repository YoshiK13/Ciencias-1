import random

array = random.sample(range(2000),1000)
n = 0

def insertion_sort(arr):
    global n

    for i in range(1, len(arr)):
        # Llave y primer dato a comparar
        key = arr[i]
        j = i - 1
        n += 2

        # mover datos a la derecha si son mayores a la clave hasta insertar la clave  
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            n += 4

        arr[j + 1] = key
        n += 1

insertion_sort(array)
print(array, n)