# Faça um Algoritmo que leia 5 valores inteiros e escreva no final a soma dos valores lidos.

def main():
    a = 0
    cont = 0
    soma = 0
    for cont in range (0, 5, 1):
        a = int(input())
        soma = soma+a
    print(soma)
    return 0

if __name__ == "__main__":
    main()
