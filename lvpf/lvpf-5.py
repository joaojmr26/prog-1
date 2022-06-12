# Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721. Usar, exclusivamente, DIV e MOD.

def f_cont(n):
    cont = 0
    while (n>0):
        n = n // 10
        cont += 1
    return cont

def f_inv(n):
    valor = 0
    tam = f_cont(n)
    p = tam - 1
    while (n > 0):
        resto = n%10
        valor += resto *10 ** p
        p = p - 1
        n = n//10
    return valor

def main():
    n = int(input())
    valor = f_inv(n)
    print(valor)
    return 0

if __name__ == "__main__":
    main()
