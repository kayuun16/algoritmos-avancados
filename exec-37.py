# 37) Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Morango  Até 5 Kg = R$ 2,50 por Kg / Acima de 5 Kg = R$ 2,20 por Kg
# Maçã Até 5 Kg R$ 1,80 por Kg  / Acima de 5 Kg = R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
# ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
# morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_morango = int(input('Deseja comprar quantos kg de morango? '))
kg_maca = int(input('Deseja comprar quantos kg de maca? '))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.5
else:
    preco_morango = kg_morango * 2.2
    
if kg_maca <= 5:
    preco_maca = kg_maca * 1.8
else:
    preco_maca = kg_maca * 1.5
    
valor_total = preco_morango + preco_maca
kg_total = kg_morango + kg_maca

desc = (10/100) * valor_total

if valor_total > 25 or kg_total > 8:
    valor_total -= desc
    print(f'Preco total: R$ {valor_total}')
else:
    print(f'Preco total: R$ {valor_total}')