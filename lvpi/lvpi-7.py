# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.
def main():
    a = int(input())
    b = int(input())
    p1 = a+((b*a)/100)
    print( p1 )
    return 0
if __name__ == "__main__":
    main()