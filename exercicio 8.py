#8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
#Inputs
#Qual a quantidade de votos brancos?
#nulos?
#válidos?
#============================================
#Output
#Total de porcentagens
#Total de votos válidos: x%
#Total de votos em branco: y%
#Total de votos nulos: t%

print("Qual a quantidade de votos brancos?")
votos_branco = int(input())

print("Qual a quantidade de votos nulos?")
votos_nulos = int(input())

print("Qual a quantidade de votos validos?")
votos_validos = int(input())

votos_totais = votos_validos + votos_nulos + votos_branco

validos_percentual = (votos_validos / votos_totais) * 100

branco_percentual = (votos_branco / votos_totais) * 100

nulos_percentual = (votos_nulos / votos_totais) * 100 

print("Total de Porcentagens:")

print(f"Total de votos validos: {validos_percentual:.2f} %")
print(f"Total de votos em branco: {branco_percentual:.2f} %")
print(f"Total de votos nulos: {nulos_percentual:.2f} %")
