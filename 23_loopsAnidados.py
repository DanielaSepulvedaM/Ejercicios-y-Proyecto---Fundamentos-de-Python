matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matriz[0])
print(matriz[0][1])

#iteracion -> ciclo anidado
for row in matriz:
    print(row)
    for column in row:
        print(column)
