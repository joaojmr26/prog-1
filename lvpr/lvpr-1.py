# Faça um Algoritmo para ler um valor N e imprimir todos os valores inteiros entre 1
# (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO. UTILIZE O COMANDO WHILE.

def main():
    n = int(input())
    a = (n+1)
    b = 0
    for b in range (1, a ):
        print(b)
    return 0

if __name__ == "__main__":
    main()
