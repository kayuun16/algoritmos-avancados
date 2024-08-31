# 73) A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:

#a) Média de salário da população
#b) Média do número de filhos
#c) Maior salário dos habitantes
#d) Percentual de pessoas com salário menor que R$ 150,00

#Obs.: O final da leitura dos dados se dará com a entrada de um “salário negativo”.

maior_salario = 0
total_salario = 0
total_filho = 0
qtd_populacao = 0
pessoas_salario_menor_150 = 0

while True:
    salario = float(input('Digite seu salario: '))
    filho = int(input('Quantos filhos voce tem? '))
    
    if salario < 0:
        break
    
    total_salario += salario
    total_filho += filho
    qtd_populacao += 1
    
    if maior_salario == 0 or maior_salario < salario:
        maior_salario = salario
    
    if salario < 150:
        pessoas_salario_menor_150 += 1
        
media_salario = total_salario / qtd_populacao
media_filho = total_filho / qtd_populacao
percentual_salario_menor_150 = (pessoas_salario_menor_150 / qtd_populacao) * 100

print(f'Media de salario da populacao: R$ {media_salario:.2f}')
print(f'Media do numero de filhos: {media_filho:.0f}')
print(f'Maior salario dos habitantes: R$ {maior_salario:.2f}')
print(f'Percentual de pessoas com salario menor que R$ 150,00: {percentual_salario_menor_150:.2f}%')