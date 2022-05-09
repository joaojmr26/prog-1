# Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). 
# Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

def main():
    h1 = int(input())
    h2 = int(input())
    m1 = int(input())
    m2 = int(input())
    if (h1 > h2): 
        hmv = h1
        hmn = h2
    else:
        hmv = h2
        hmn = h1

    if (m1 > m2): 
        mmv = m1
        mmn = m2
    else:
        mmv = m2
        mmn = m1

    print(hmv+mmn, hmn*mmv)

    return 0

if __name__ == "__main__":
    main()
