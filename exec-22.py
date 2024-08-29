# 22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
jornada_mensal = 160

print("Quantas horas trabalhou esse mes?")
horas_trab_mensal = int(input())

print("Qual o salario por hora trabalhada?")
salario_hora_trab = float(input())

hora_extra = horas_trab_mensal - jornada_mensal
salario_extra = ((50/100) * salario_hora_trab) * hora_extra
salario_regular = horas_trab_mensal * salario_hora_trab

if horas_trab_mensal == jornada_mensal:
    salario_final = salario_regular
    print("Salario regular: R$" + str(salario_regular))
    print("Salario final: R$" + str(salario_final))
elif horas_trab_mensal > jornada_mensal:
    salario_final = salario_regular + salario_extra
    print("Salario regular: R$" + str(salario_regular))
    print("Salario por hora extra: R$" + str(salario_extra))
    print("Salario final: R$" + str(salario_final))
else:
    salario_final = salario_regular
    print("Salario final: R$" + str(salario_final))
    print("JORNADA SEMANAL NAO ATINGIDA!")
