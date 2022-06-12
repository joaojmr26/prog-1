# Fazer um programa que calcule e escreva o valor de S:
# S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 ... - 10/100

def main():
    s = 0
    for n in range(1,11):
        if(n%2 == 0):
            n = -n
        else:
            n = n
        s = s + (n/(n**2))
        n = n*-1
    print(s)
    return 0

if __name__ == "__main__":
    main()