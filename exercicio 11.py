#11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

print("Quantos carros vendeu esse mes?")
carros_vendidos = int(input())

print("Qual o valor total das vendas?")
vendas_total = float(input())

print("Qual o seu salario fixo mensal?")
salario_fixo = float(input())

bonus_por_carro = carros_vendidos * 700

bonus_percentual = (5/100) * vendas_total

salario_final = salario_fixo + bonus_por_carro + bonus_percentual

print("Salario final: " + str(salario_final))