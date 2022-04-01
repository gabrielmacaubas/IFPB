valores = [4, 5, 3, 6, 10]  # 5 elementos

while True:
    index = int(input('Índice do array:'))
    if index < 0:
        break
    try:
        print(f'List[{index}] = {valores[index]}')
    except IndexError:
        print("Posição fora do intervalo do array")
    except IndexError:
        print("XYZ")
