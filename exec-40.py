# 40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%

print("Nome do produto:")
nome_prod = str(input())

print("Quantidade adquirida do produto:")
qtd_prod = int(input())

print("Qual o valor unitario do produto?")
valor_prod = float(input())

total = qtd_prod * valor_prod

if qtd_prod <= 5:
    desconto = (2 / 100) * total
elif qtd_prod > 5 and qtd_prod <= 10:
    desconto = (3 / 100) * total
else:
    desconto = (5 / 100) * total
    
total_a_pagar = total - desconto

print("Total: R$" + str(total))
print("Desconto: R$" + str(desconto))
print("Total a pagar: R$" + str(total_a_pagar))
