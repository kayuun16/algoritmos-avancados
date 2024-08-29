# 12) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo): 
# C / 5 = (F - 32) / 9

print("Digite a temperatura em Fahrenheit: ")
temp_fah = float(input())

temp_celsius = ((temp_fah - 32) / 9) * 5

print("Temperatura em Celsius: " + str(temp_celsius))
