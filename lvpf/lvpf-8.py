#Função MDC

def f_mdc(n1,n2,n3):
    maior = 0
    if(n1 > n2 and n1 > n3):
        maior = n1
    elif(n2 > n3 and n2 > n1):
        maior = n2
    elif(n3 > n2 and n3 > n1):
        maior = n3

    mdc = maior
    while (n1 % mdc != 0 or n2 % mdc != 0 or n3 % mdc != 0):
        mdc = mdc -1
    
    return(mdc)

#Função Principal

def main():
    for i in range(5):
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        mdc = f_mdc(n1,n2,n3)
        print(f'MDC{n1,n2,n3}={mdc}')

    return 0

if __name__ == "__main__":
    main()
