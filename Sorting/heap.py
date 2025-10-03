import random

array = random.sample(range(2000),1000)
test = [9, 4, 3, 8, 10, 2, 5]
n = 0 # pasos

def heapify(arr, size, index):
    global n

    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    n += 3

    if (left < size) and (arr[left] > arr[largest]):
        largest = left
        n += 1

    if (right < size) and (arr[right] > arr[largest]):
        largest = right
        n += 1

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]

        heapify(arr, size, largest)
        n += 2

    n += 5

def heap_sort(arr):
    global n

    size = len(arr)
    n += 1

    #recorrer desde abajo hacia arriba todo el arbol para mover los mayores (alistar array)
    for i in range(size//2 - 1, -1, -1):
        heapify(arr, size, i)
        n += 1

    # Ordenar array
    for i in range(size - 1, 0, -1):
        #raiz del todo el arbol se pone al final (ordenar dato mayor)
        arr[0], arr[i] = arr[i], arr[0]

        #volver a poner el mayor en la raiz
        heapify(arr, i, 0)
        n += 2

heap_sort(array)
print(array, n)