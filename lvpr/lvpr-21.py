def main():
    n_oper = 0
    cond = str(input())
    soma, sub, mult, div, exp, raiz = int(0), int(0), int(0), int(0), int(0), int(0)
    invalida = int(0)
    while(cond == "s"):
        n_oper = int(input())
        if(n_oper < 7):
            n1 = int(input())
            n2 = int(input())
            if(n_oper == 1):
                soma = n1+n2
            elif(n_oper == 2):
                sub = n1-n2
            elif(n_oper == 3):
                mult = n1*n2
            elif(n_oper == 4):
                div = n1/n2
            elif(n_oper == 5):
                exp = n1**n2
            elif(n_oper == 6):
                raiz = n1**(1/n2)
        else:
            invalida += 1
        cond = str(input())
    print(soma)
    print(sub)
    print(mult)
    print(div)
    print(exp)
    print(raiz)
    if(invalida > 0):
        for i in range(invalida):
            print("OPERACAO INVALIDA")


if __name__ == "__main__":
    main()