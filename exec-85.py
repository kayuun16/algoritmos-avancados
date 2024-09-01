# 85) Faça um algoritmo para ler e armazenar em um vetor a temperatura média de todos os dias do ano. Calcular e escrever: 

# a) Menor temperatura do ano
# b) Maior temperatura do ano
# c) Temperatura média anual
# d) O número de dias no ano em que a temperatura foi inferior a média anual

temperaturas = [None] * 5
qtd_temperaturas = 0
soma_temperaturas = 0
dias_abaixo_media = 0

for i in range(5):
    temperaturas[i] = float(input(f'Digite a temperatura media do dia {i + 1}: '))
    qtd_temperaturas += 1
    soma_temperaturas += temperaturas[i]
    media_anual = soma_temperaturas / qtd_temperaturas
    if temperaturas[i] < media_anual:
        dias_abaixo_media += 1
    
maior_temperatura = max(temperaturas)
menor_temperatura = min(temperaturas)

print(f'Menor temperatura do ano: {menor_temperatura:.1f}° C')
print(f'Maior temperatura do ano: {maior_temperatura:.1f}° C')
print(f'Temperatura média anual: {media_anual:.1f}° C')
print(f'Numero de dias com temperatura abaixo da média anual: {dias_abaixo_media}')