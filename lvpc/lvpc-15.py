# Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos), em formato 24h. 
# Calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

def main():
    i = int(input())
    f = int(input())
    if (i >= f):
        duracao = 24 - i + f
    else:
        duracao = f-i
    print(duracao)
    return 0
if __name__ == "__main__":
    main()