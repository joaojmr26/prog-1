# Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo e qual tipo de triângulo é. 
# OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    if (a >= b + c or b >= a + c or c >= a + b):
        print("NÃO É TRIÂNGULO")
    elif (a == b and b == c):
        print("EQUILÁTERO")
    elif (a == b or b == c or c == a):
        print("ISÓSCELES")
    else:
        print("ESCALENO")
    return 0
if __name__ == "__main__":
    main()