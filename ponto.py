import random

dias = int(input("Digite a quantidade de dias que sera gerado: "))

entrada= [ "08:55", "08:56", "08:57", "08:56","08:58", "08:59", "09:00", "09:01", "09:03", "09:04", "09:05"]
saida= [ "17:55", "17:56", "17:57", "17:56","17:58", "17:59", "18:00", "18:01", "18:03", "18:04", "18:05"]

horarios = []

for dia in range(dias):
    selectedEntrada = random.randrange(0, (len(entrada)))      
    selectedSaida =random.randrange(0, (len(saida)))
    horarios.append({'dia':dia+1, 'entrada': entrada[selectedEntrada], "saida" : saida[selectedSaida] })

for horario in horarios:
    print(horario)      
