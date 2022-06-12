# Tem-se um conjunto de dados contendo o sexo (masculino, feminino) e a altura de 5 pessoas. 
# Fazer um algoritmo que calcule e escreva:
# - a maior e a menor altura do grupo;
# - a média de altura das mulheres;
# - a quantidade de homens;

def main():
    altmul = 0
    contm = 0
    conth = 0
    primeiro = True
    alto = 0
    baixo = 10
    for i in range(1, 6):
        sexo = input()
        altura = float(input())
        if(sexo.upper() == "F"):
            altmul = altmul + altura
            contm = contm + 1
        elif(sexo.upper() == "M"):
            conth = conth + 1
        if(altura > alto):
            alto = altura
        elif(altura < baixo):
            baixo = altura
    print(alto, baixo, altmul/contm, conth)
    return 0
    
if __name__ == "__main__":
    main()