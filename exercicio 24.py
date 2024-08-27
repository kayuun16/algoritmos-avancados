# 24) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

print("Qual o seu salario mensal fixo?")
salario_fixo = float(input())

print("Quanto foi o valor de vendas totais desse mes?")
valor_vendas = float(input())

comissao = (3 / 100) * valor_vendas
bonus_vendas = valor_vendas - 1500
bonus = (5 / 100) * bonus_vendas

if valor_vendas <= 1500:
    salario_final = salario_fixo + comissao
else:
    salario_final = salario_fixo + comissao + bonus
    
print("Salario final: R$" + str(salario_final))