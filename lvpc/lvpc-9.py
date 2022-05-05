# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos dois maiores valores.

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    maior1 = a
    maior2 = a
    if (maior1<b and maior1>c):
        maior1=b
    else:
        maior1=c
    print (maior1)
    if (maior2<c):
        maior2=c
    else:
        maior2=a
    print (maior1+maior2)
    return 0
if __name__ == "__main__":
    main()