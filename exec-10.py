# 10) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

print("Qual o custo de fabrica do carro:")
custo_fabrica = float(input())

distribuidor = (28/100) * custo_fabrica

imposto = (45/100) * custo_fabrica

custo_consumidor = custo_fabrica + distribuidor + imposto

print("Custo final do carro: " + str(custo_consumidor))
