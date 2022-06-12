# Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. 
# A última linha que não entrará nos cálculos, contém o valor da idade igual a zero.
# Calcule e escreva a idade média deste grupo de indivíduos.

def main():
    idade = int(input())
    contidade = 0
    cont = 0
    while(idade != 0):
        contidade += idade
        cont += 1
        idade = int(input())
    print(contidade/cont)
if __name__ == "__main__":
    main()