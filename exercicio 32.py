# 32) Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

print("Qual o nome do time?")
time1 = str(input())

print("Qual o nome do time adversario?")
time2 = str(input())

print("Quantos gols " + str(time1), "marcou?")
gols_time1 = int(input())

print("Quantos gols " + str(time2), "marcou?")
gols_time2 = int(input())

if gols_time1 > gols_time2:
    print(str(time1) + " venceu!")
elif gols_time1 == gols_time2:
    print("Empate!")
else:
    print(str(time2) + " venceu!")