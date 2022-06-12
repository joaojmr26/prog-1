# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def qntd(arg):
    return(len(arg))

def main():
    arg = input()
    s = qntd(arg)
    print(s)
    return 0

if __name__ == "__main__":
    main()
