# 72) Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever: 
#- o maior preço lido
#- a média aritmética dos preços dos produtos

soma = 0
maior_preco = 0

for i in range(1, 16):
    cod_produto = str(input(f'Digite o codigo do produto {i}: '))
    preco_produto = float(input(f'Digite o preco do produto {i}: '))
    soma += preco_produto
    
    if maior_preco == 0 or maior_preco < preco_produto:
        maior_preco = preco_produto
        
media = soma / 15

print(f'Maior preco: R${maior_preco}')
print(f'Media aritmetica dos precos dos produtos: {media:.2f}')
