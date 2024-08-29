# 21) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

print("Que horas o jogo comecou? (0 hrs - 23 hrs)")
hora_inicio = int(input())

print("Que horas o jogo terminou? (0 hrs - 23 hrs)")
hora_fim = int(input())

duracao_jogo = 0

if hora_inicio > 23 or hora_fim > 23:
    print("Tempo de jogo invalido! As horas de inicio e fim de jogo devem estar entre 0-23")
elif hora_fim >= hora_inicio:
    duracao_jogo = hora_fim - hora_inicio
    print("A duracao do jogo foi de: " + str(duracao_jogo), " horas")
else:
    if hora_fim < hora_inicio:
        duracao_jogo = (24 - hora_inicio) + hora_fim
        print("A duracao do jogo foi de: " + str(duracao_jogo), " hora(s)")