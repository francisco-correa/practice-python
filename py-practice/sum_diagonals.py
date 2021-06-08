n = 3
matriz = [[11, 2, 4], [4, 5, 6], [10, 8, -12]] 
sumaDiagonales = 0

for x in range(0,3):
    sumaDiagonales = sumaDiagonales + matriz[x][x]
    if (x != 1):
        sumaDiagonales = sumaDiagonales + matriz[x][2-x]

print("La suma es:" + str(sumaDiagonales))
print(matriz)

def diagonalDifference(arr):
    rightDiag, leftDiag = 0, 0
    i = 0
    j = 0
    len_array = len(arr)
    
    while (i < len(arr)):
        leftDiag += arr[i][j]
        i += 1
        j += 1
        
    i= 0
    j = len_array - 1
    while (i < len(arr)):
        rightDiag += arr[i][j]
        i += 1
        j -= 1
    
    return(abs(leftDiag - rightDiag))

print(diagonalDifference([[1,2,3], [3,2,3], [4,5,1]]))
