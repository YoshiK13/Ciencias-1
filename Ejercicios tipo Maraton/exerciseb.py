import numpy
import itertools


# Inicializa la lista de resultados
distResults = []


# Bucle principal
while True:
    pointQuantity = int(input())
    if pointQuantity == 0:
        break

    matrix = []
    for i in range(pointQuantity):
        row = []
        for j in range(2):
            row.append(int(input()))
        matrix.append(row)

    newlst = []
    for pair in itertools.combinations(matrix, 2):
        dist = numpy.sqrt((pair[1][0] - pair[0][0]) ** 2 + (pair[1][1] - pair[0][1]) ** 2)
        newlst.append(round(dist, 4))

    if newlst:
        if min(newlst) >= 10000:
            distResults.append("INFINITY")
        else:
            distResults.append(min(newlst))
    else:
        distResults.append(None)


for i in distResults:
    if i is not None:
        print(i)
    else:
        print("No hay combinaciones posibles para este caso.")