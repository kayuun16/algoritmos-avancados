# 16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("Quantas macas deseja comprar?")
total_macas = int(input())

if total_macas < 12:
    total_macas = total_macas * 1.3
else:
    total_macas = total_macas * 1
    
print("O valor total e : R$" + str(total_macas))
