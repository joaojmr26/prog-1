#Gerador e Validador de Cpf
 
import random

# Função calculando o primeiro digito verificador
def f_dig1(d1,d2,d3,d4,d5,d6,d7,d8,d9):
    soma = (d1*10)+(d2*9)+(d3*8)+(d4*7)+(d5*6)+(d6*5)+(d7*4)+(d8*3)+(d9*2)
    div = soma%11
    if(div < 2):
        dv1 = 0
    else:
        dv1 = 11 - div
    return(dv1)
    
# Função calculando o segundo digito verificador
def f_dig2(d1,d2,d3,d4,d5,d6,d7,d8,d9,dv1):
    soma = (d1*11)+(d2*10)+(d3*9)+(d4*8)+(d5*7)+(d6*6)+(d7*5)+(d8*4)+(d9*3)+(dv1*2)
    div = soma%11
    if(div < 2):
        dv2 = 0
    else:
        dv2 = 11 - div
    return(dv2)

def main():
    continuar = True #Condição de Parada

    while(continuar == True):
        #Definindo qual função irá usar
        print("[1] Validador de Cpf")
        print("[2] Gerador de Cpf")
        print("[3] Fechar o Programa")
        fn = input("Função Escolhida: ")

        if(fn == "1"):
            print("Utilize o formato 123.456.789-10")
            cpf = input("Cpf: ")
            continuar = True
            uso = True
        elif(fn == "2"):
            print("Gerando Cpf...")
            #Gerando CPF aleatório
            nale = random.getrandbits(32)
            nale = str(nale)
            cpf = str(nale[0:3]+"."+nale[3:6]+"."+nale[6:9]+"-00")
            continuar = True
            uso = True
        elif(fn =="3"):
            continuar = False
            uso = False
        else:
            print(" ")
            print("Utilize os números 1/2/3 para definir o que você gostaria de utilizar")
            continuar = True
            uso = False

        if(uso == True):
            #Separando os termos do cpf
            d1, d2, d3, d4, d5, d6, d7, d8, d9, = int(cpf[0]), int(cpf[1]), int(cpf[2]), int(cpf[4]), int(cpf[5]), int(cpf[6]), int(cpf[8]), int(cpf[9]), int(cpf[10])
            dv = str(cpf[12:14])
        
            #Digitos verificadores calculados
            dv1 = f_dig1(d1,d2,d3,d4,d5,d6,d7,d8,d9)
            dv2 = f_dig2(d1,d2,d3,d4,d5,d6,d7,d8,d9,dv1)
            dvcalc = str(dv1)+str(dv2)

            #Juntando números com os digitos do cpf
            cpfvalido = str(cpf[0:12]+dvcalc)

            #Outputs das funções
            if(fn == "1"):
                print("Validando Cpf...")
                if(cpf == cpfvalido):
                    print("Cpf Válido!")
                    print(" ")
                else:
                    print("Cpf Inválido!")
                    print(" ")
            elif(fn == "2"):
                print("Cpf Gerado: ", cpfvalido)
                print(" ")

        elif(uso == False): #Verifica o motivo de nenhuma função ter sido usada
            if(fn == "3"):
                print("Finalizando o programa...")
            else:
                print("Reiniciando o Programa...")
                print(" ")
if __name__ == "__main__":
    main()