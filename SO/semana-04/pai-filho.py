import os
x = 10
print('blz?')
retorno = os.fork()

if retorno == 0:
    print('Sou o filho com pid', os.getpid(), x)
else:
    os.wait()
    print('Sou o pai', os.getpid(), 'Criei o filho', retorno)

