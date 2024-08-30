# 56) Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

valor = int(input("Digite um valor entre 1 e 10:"))

while valor < 1 or valor > 10:
    valor = int(input("Valor invalido. Digite um valor entre 1 e 10:"))
    
for i in range (1, 11):
        tabuada = valor * i
        print(f"{valor} x {i} = {tabuada}")