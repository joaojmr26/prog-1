# Faça um programa que leia um número inteiro e diga se ele é par ou ímpar.

def main():
    n = int(input())
    if (n%2) == 0:
        print("PAR")
    else:
        print("IMPAR")
    
    return 0
if __name__ == "__main__":
    main()