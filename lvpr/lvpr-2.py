# Faça um Algoritmo para ler um valor inteiro e escrever a tabuada de 1 a 10 do valor lido. UTILIZE O COMANDO FOR.

def main():
    n = int(input())
    a = (n+1)
    b = 0
    for b in range (1, 11 ):
        r = n*b
        print(b, "x", n, "=", r)
    return 0

if __name__ == "__main__":
    main()
