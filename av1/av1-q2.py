# Faça um programa que, dados 4 números inteiros com entrada, apresenta a soma do maior e do menor valor.

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    nmaior = 0
    if(n1>n2 and n1>n3 and n1>n4):
        nmaior = n1
    elif(n2>n3 and n2>n4):
        nmaior = n2
    elif(n3>n4):
        nmaior = n3
    else:
        nmaior = n4
    if(n1<n2 and n1<n3 and n1<n4):
        nmenor = n1
    elif(n2<n3 and n2<n4):
        nmenor = n2
    elif(n3<n4):
        nmenor = n3
    else:
        nmenor = n4
    calc = (nmaior+nmenor)
    print(calc)
main()
