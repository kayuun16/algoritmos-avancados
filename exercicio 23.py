# 23) Para o enunciado a seguir foi elaborado um algoritmo em Português Estruturado que contém erros, identifique os erros no algoritmo apresentado abaixo: Enunciado: Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas:

#- para sexo masculino: peso ideal = (72.7 * altura) - 58
#- para sexo feminino: peso ideal = (62.1 * altura) - 44.7

#inicio
#ler nome
#ler sexo
#se sexo = M então
#       peso_ideal = (72.7 * altura) - 58
#senão peso_ideal = (62.1 * altura) – 44.7
#fim_se
#escrever peso_ideal
#fim

print("Qual o seu nome?")
nome = str(input())

print("Qual a sua altura? (em metros)")
altura = float(input())

print("Qual o seu sexo? ('M' para masculino ou 'F' para feminino)")
sexo = str(input())

if sexo == "M" or sexo == "m":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal: {peso_ideal:.2f} kg")
elif sexo == "F" or sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal: {peso_ideal:.2f} kg")
else:
    print("Ocorreu um ERRO!")