# Faça um Programa que leia números até que o usuário não queira mais digitar os números. 
# No final escrever a soma dos valores lidos. 
# (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)

def main():
    a = input()
    c = 0
    while(a != "n"):
        b = int(input())
        a = input()
        c += b
    print(c)
    return 0

if __name__ == "__main__":
    main()
