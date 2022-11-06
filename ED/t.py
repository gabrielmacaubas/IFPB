def decodeString(numberOfRows, encodedString):
    colunas = int(len(encodedString)/numberOfRows)
    matriz = [[None] * (colunas) for i in range(numberOfRows)]
    cont = 0

    for i in range(numberOfRows):
        for j in range(colunas):
            matriz[i][j] = encodedString[cont]
            cont += 1

    string = ""
    x = 0
    
    for i in range(colunas):
        for j in range(numberOfRows):
            if x == colunas:
                break

            if matriz[j][x] == "_":
                string += " "

            else:

                string += matriz[j][x]
            
            if x != colunas:
                x += 1

        x = i + 1
        
    return string
    

if __name__ == '__main__':
    numberOfRows = 2
    encodedString = "hlowrd_el_ol"
    result = decodeString(numberOfRows, encodedString)
    print(result)
