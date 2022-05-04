# Faça um programa que leia um valor inteiro com três casas decimais e, utilizando recursos que já aprendemos em sala de aula, inverta esse número, entregando um valor inteiro de três casas decimais (PROIBIDO UTILIZAR QUALQUER RECURSO DE STRING). 
# Ao final, o programa deverá verificar se o valor digitado é um PALÍNDROMO.

def main():
    nent = int(input())
    c = nent//100
    d = (nent//10) - (c*10)
    n = nent%10
    ninv = (n*100) + (d*10) + c
    if(ninv == nent):
        print( nent, "É UM PALÍNDROMO")
    else:
        print( nent, "NÃO É UM PALÍNDROMO")
main()
