# 42) Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 

# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

#Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

print("Digite seu codigo:")
cod = int(input())

print("Digite seu ano de nascimento:")
ano_nasc = int(input())

print("Digite o ano que ingressou na empresa:")
ingresso = int(input())

idade = 2024 - ano_nasc
anos_trab = 2024 - ingresso

print("Idade: " + str(idade), "anos")
print("Anos de trabalho na empresa: " + str(anos_trab), "ano(s)")

if idade >= 65 or anos_trab >= 30 or (idade >= 60 and anos_trab >= 25):
 print("Requerer aposentadoria")
else:
 print("Não requerer aposentadoria")
