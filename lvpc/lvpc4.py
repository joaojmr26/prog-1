# Ler quatro valores referentes a quatro notas escolares (0 a 100) de um aluno e escrever uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 60.

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    media = (a+b+c+d/4)
    if media>=60 :
        print("APROVADO")
    else:
        print("REPROVADO")
    
    return 0
if __name__ == "__main__":
    main()