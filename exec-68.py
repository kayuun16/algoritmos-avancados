# 68) Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das mercadorias.

valor_total_mercadorias = 0

total_mercadorias = int(input('Qual o total de mercadorias em estoque?'))

for i in range(1, total_mercadorias + 1):
    valor_mercadoria = float(input(f'Qual o valor da mercadoria {i}?'))
    valor_total_mercadorias += valor_mercadoria
    
media = valor_total_mercadorias / total_mercadorias

print(f'Media aritmetica do valor de todas as mercadorias em estoque: {media:.2f}')