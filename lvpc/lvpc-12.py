# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a > b and a > c):
        print(a)
    elif (b > c ):
        print(b)
    else:
        print(c)
    return 0
if __name__ == "__main__":
    main()