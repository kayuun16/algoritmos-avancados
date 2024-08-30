# 69) O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque. Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor das mercadorias em estoque.

valor_total_mercadorias = 0
total_mercadorias = 0

while True:
    valor_mercadoria = float(input(f'Qual o valor da mercadoria?'))
    valor_total_mercadorias += valor_mercadoria
    total_mercadorias += 1
    continuar = str(input('Mais mercadorias? (S/N)')).upper()
    
    if continuar != 'S':
        break
    
media = valor_total_mercadorias / total_mercadorias

print(f'Media aritmetica do valor de todas as mercadorias em estoque: {media:.2f}')