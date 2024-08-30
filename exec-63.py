# 63) Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

soma = 0

for i in range (1, 11):
    valores = float(input('Digite um valor: '))
    soma += valores
    
print(f'Soma dos valores: {soma}')