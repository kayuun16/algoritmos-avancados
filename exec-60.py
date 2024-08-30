# 60) Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (inlcuindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.

cont = 1
valores_intervalo = 0
valores_fora_intervalo = 0

while cont <= 10:
    valores = int(input("Digite um valor: "))
    if valores >= 10 and valores <= 20:
        valores_intervalo += 1
    else:
        valores_fora_intervalo += 1
    cont += 1
    
print(f"Valores no intervalo [10/20]: {valores_intervalo} / Valores fora do intervalo [10/20]: {valores_fora_intervalo}")