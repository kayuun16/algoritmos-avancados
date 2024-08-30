# 49) Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do exercício [48]. Se for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá encerrar o algoritmo.

while True:
    print("Digite a nota da primeira avaliacao:")
    nota1 = float(input())
    
    print("Digite a nota da segunda avaliacao:")
    nota2 = float(input())
    
    if nota1 <= 10 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"Media: {media:.1f}")
    else:
        print("Nota Invalida")
        
    print("Novo Calculo? (S/N)")
    novo_calculo = str(input())   
        
    if novo_calculo.upper() != "S":
        break