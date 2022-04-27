# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius. Fórmula: c = (f-32)/1.8

def main():
    f = int(input())
    c = (f-32)/1.8
    print(c)
    return 0
if __name__ == "__main__":
    main()