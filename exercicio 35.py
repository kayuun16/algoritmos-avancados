# 35) Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 

print("Quantos litros deseja reabastecer?")
comb_litros = int(input())

print("Deseja qual tipo de combustivel?")
comb_tipo = str(input())

if comb_tipo == "alcool":
    comb_tipo = "A"
else:
    if comb_tipo == "gasolina":
        comb_tipo = "G"
    
if comb_litros > 20 and comb_tipo == "A":
    preco_final = (comb_litros * 2.90) - ((5 / 100) * comb_litros)
elif comb_litros > 20 and comb_tipo == "G":
    preco_final = (comb_litros * 3.30) - ((6 / 100) * comb_litros)
elif comb_litros <= 20 and comb_tipo == "A":
    preco_final = (comb_litros * 2.90) - ((3 / 100) * comb_litros)
else:
    if comb_litros <= 20 and comb_tipo == "G":
        preco_final = (comb_litros * 3.30) - ((4 / 100) * comb_litros)

print("Preco final: R$" + str(preco_final))