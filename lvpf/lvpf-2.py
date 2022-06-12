# Faça um programa que leia três número e, a partir de uma função, informe o resultado da soma, dos mesmos.

def f_soma(a,b,c):
    
    return(a+b+c)
    
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    s = f_soma(a,b,c)
    print(s)
    return 0

if __name__ == "__main__":
    main()
