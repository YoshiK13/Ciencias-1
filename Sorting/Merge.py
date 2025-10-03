import random

array=[random.randint(0,100) for i in range(1000)]

n = 0

def merge(left,right,compare):
	global n

	result = [] 
	i,j = 0,0
	n += 2

	while (i < len(left) and j < len(right)):
		if compare(left[i],right[j]):
			result.append(left[i])
			i += 1
			n += 4

		else:
			result.append(right[j])
			j += 1
			n += 4


		n += 5

	while (i < len(left)):
		result.append(left[i])
		i += 1
		n += 4

	while (j < len(right)):
		result.append(right[j])
		j += 1
		n += 4

	n += 1
	return result

def merge_sort(arr, compare = lambda x, y: x < y):
	global n

    #Utilizando la función lambda para ordenar el arreglo en orden (creciente y decreciente).
    #Por defecto ordena el arreglo en orden creciente
	if len(arr) < 2:
		n += 3
		return arr[:]

	else:
		middle = len(arr) // 2
		n += 3

		left = merge_sort(arr[:middle], compare)
		n += 2

		right = merge_sort(arr[middle:], compare)
		n += 2

		n += 2
		return merge(left, right, compare) 

print(merge_sort(array), n)