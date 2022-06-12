# Fazer um programa que calcule e escreva o valor de S:
# S = (37 x 38)/1 + (36 x 37)/2 + (35 x 36)/3 + ... + (1 x 2)/37

def main():
    mult1 = 37
    mult2 = 38
    baixo = 1
    total = 0
    while (baixo<38):
        calc1 = mult1*mult2
        calc2 = calc1/baixo
        total += calc2
        mult1 -=1
        mult2 -= 1
        baixo += 1
    print(total)
if __name__ == "__main__":
    main()