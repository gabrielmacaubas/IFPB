hora_inicio = int(input("Hora de inicio do jogo: "))
hora_final = int(input("Hora de final do jogo: "))
hora_total = int()

if hora_final > hora_inicio:
    hora_total = hora_final - hora_inicio

else:
    hora_total = (24 - hora_inicio) + hora_final


print(hora_total)
