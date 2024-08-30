# 59) Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS

cont = 1
valores_negativos = 0

while cont <= 10:
    valores = int(input("Digite um valor positivo ou negativo: "))
    if valores < 0:
        valores_negativos += 1
    cont += 1

print(f"Quantidade de valores negativos: {valores_negativos}")