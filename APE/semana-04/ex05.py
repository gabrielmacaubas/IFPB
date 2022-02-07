segundos_totais = int(input("Digite um número inteiro: "))
horas = segundos_totais // 3600
resto_horas = segundos_totais % 3600
minutos = resto_horas // 60
resto_minutos = resto_horas % 60
segundos = resto_minutos
print(horas, minutos, segundos)