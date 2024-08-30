# 71) Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade de números. Depois de ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos e a média dos números lidos.

soma = 0
maior_valor = 0
qtd_valores = int(input('Quantos numeros?'))

for i in range(1, qtd_valores + 1):
    valor = float(input(f'Digite o valor do numero {i}: '))
    soma += valor
    
if maior_valor == 0 or maior_valor < valor:
    maior_valor = valor
    
media = soma / qtd_valores
    
print(f'Maior valor dentre os {qtd_valores} valores: {maior_valor}')
print(f'Media aritmetica dos valores: {media:.2f}')
