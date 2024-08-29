# 25) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
print("Numero da conta:")
num_conta = int(input())

print("Saldo da conta:")
saldo = float(input())

print("Debito da conta:")
debito = float(input())

print("Credito da conta:")
credito = float(input())

saldo_atual = float(saldo - debito + credito)

print(saldo_atual)

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
