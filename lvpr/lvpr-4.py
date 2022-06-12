# Faça um Programa que leia números até que o usuário não queira mais digitar os números. 
# No final escrever a média dos valores lidos. 
# (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)

def main():
    a = input()
    c = 0
    d = 0
    e = 0
    while(a != "n"):
        b = int(input())
        a = input()
        c += b
        d += (b - (b-1))
    e = c/d
    print(e)
    return 0

if __name__ == "__main__":
    main()
