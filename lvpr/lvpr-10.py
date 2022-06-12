# Faça um Algoritmo que leia 5 valores e escreva no final a soma dos valores positivos e a média dos negativos. 

def main():
    a = 0
    cont = 0
    contneg = 0
    somaneg = 0
    soma = 0
    for cont in range (0, 5, 1):
        a = int(input())
        if a>=0:
            soma = soma+a
        else:
            contneg = contneg+1
            somaneg = somaneg+a
            media = somaneg/contneg
    print(soma, media)
    return 0

if __name__ == "__main__":
    main()
