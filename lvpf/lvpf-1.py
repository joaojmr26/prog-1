# Faça um programa que leia dois número e, a partir de uma função, informe o resultado da soma, dos mesmos.

def f_soma(a,b):
    
    return(a+b)
    
def main():
    a = int(input())
    b = int(input())
    s = f_soma(a,b)
    print(s)
    return 0

if __name__ == "__main__":
    main()
