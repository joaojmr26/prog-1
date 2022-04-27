# Faça um programa que receba um número inteiro de 3 dígitos e apresente esse número ao contrário. Ex: 123 >> 321  ;  981 >> 189

def main():
    a = int(input())
    dig1 = int(a/100)
    dig2 = int(a/10 - (dig1*10))
    dig3 = int(a - (dig2*10) - (dig1*100))
    print ( (dig3*100) + (dig2*10) + dig1 )
    return 0
if __name__ == "__main__":
    main()