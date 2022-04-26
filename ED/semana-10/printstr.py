# print recursivo printstr()
def printstr(str):
    if ( str == ''):
        return
    print(str[0], end='')
    printstr( str[1:])

def printstrinvertida(str):
    if ( str == ''):
        return    
    printstrinvertida( str[1:])
    print(str[0], end='')

def tamanhostr(str):
    if ( str == ''):
        return 0
    else:
        return 1 + tamanhostr(str[1:])

str = 'curso superior de tecnologia em sistemas para internet'
printstr(str)
print()
printstrinvertida(str)
print()
print('tamanho: ', tamanhostr(str))