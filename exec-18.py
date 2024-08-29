# 18) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
print("Qual o ano atual?")
ano_atual = int(input())

print("Em que ano voce nasceu?")
ano_nasc = int(input())

idade_votar = ano_atual - ano_nasc

if idade_votar >= 18:
    print("Voce pode votar esse ano!")
else:
    print("Voce nao pode votar esse ano!")
