def voraz_value(arr):
    if not arr:
        return 0
    n = len(arr)
    if n == 1:
        return arr[0]
    a, b = 0, arr[0]
    for i in range(1, n):
        a, b = b, max(b, a + arr[i])
    return b

def main():
    import sys
    data = sys.stdin.read().split()
    index = 0
    resultados = []
    
    while index < len(data):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        if n == 0 and m == 0:
            break
            
        grid = []
        for i in range(n):
            row = list(map(int, data[index:index+m]))
            index += m
            grid.append(row)
        
        row_values = []
        for i in range(n):
            row_values.append(voraz_value(grid[i]))
        
        if n == 0:
            resultados.append(0)
        elif n == 1:
            resultados.append(row_values[0])
        else:
            a, b = 0, row_values[0]
            for i in range(1, n):
                a, b = b, max(b, a + row_values[i])
            resultados.append(b)
    
    for res in resultados:
        print(res)

if __name__ == "__main__":
    main()