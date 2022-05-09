# Desenvolva um programa que receba dois valores para efetuar operações matemáticas de acordo com a opção do usuário, 1 para soma, 2 para subtração (do primeiro pelo segundo), 3 para multiplicação, 4 para divisão (do primeiro pelo segundo), 5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice). 
# Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.

def main():
    op = int(input("Operação: "))
    if (op > 0 and op < 7):
        a = float(input("a: "))
        b = float(input("b: "))
    if (op == 1):
        print(a+b)
    elif (op == 2):
        print(a-b)
    elif (op == 3):
        print(a*b)
    elif (op == 4):
        print(a/b)
    elif (op == 5):
        print(a**b)
    elif (op == 6):
        print(a**(1/b))
    else:
        print("OPERACAO INVALIDA")
    return 0

if __name__ == "__main__":
    main()
