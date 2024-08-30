# 61) Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

cont = 1
soma = 0

while cont <= 10:
    valores = float(input("Digite um valor: "))
    soma += valores
    cont += 1
    
media = soma / 10

print(f"Media aritmetica dos valores: {media:.2f}")