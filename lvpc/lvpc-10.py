# Ler 3 valores inteiros (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a < b and b < c):
        print(a,b,c)
    elif (a < c and c < b):
        print(a,c,b)
    elif (b < a and a < c):
        print(b,a,c)
    elif (b < c and c < a):
        print(b,c,a)
    elif (c < a and a < b):
        print(c,a,b)
    else:
        print(c,b,a)

main()