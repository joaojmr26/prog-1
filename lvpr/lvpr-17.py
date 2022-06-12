# Fazer um programa que calcule e escreva o valor de S:
# S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

def main():
    cima = float(1)
    baixo = float(1)
    total = 0
    while (baixo<51):
        calc = cima/baixo
        total += calc
        cima +=2
        baixo += 1
    print(total)
if __name__ == "__main__":
    main()