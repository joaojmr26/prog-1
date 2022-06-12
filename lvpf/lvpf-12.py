#Faça um programa que, dados os nove primeiros números e os dois dígitos verificadores, 
# informe se o CPF é válido ou inválido

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
    cpf = input()
    #Separando os termos do cpf
    d1, d2, d3, d4, d5, d6, d7, d8, d9, = int(cpf[0]), int(cpf[1]), int(cpf[2]), int(cpf[4]), int(cpf[5]), int(cpf[6]), int(cpf[8]), int(cpf[9]), int(cpf[10])
    dv = str(cpf[12:14])
    
    #Digitos verificadores calculados
    dv1 = f_dig1(d1,d2,d3,d4,d5,d6,d7,d8,d9)
    dv2 = f_dig2(d1,d2,d3,d4,d5,d6,d7,d8,d9,dv1)
    dvcalc = str(dv1)+str(dv2)
    #Verificando a validade do cpf
    if(dv == dvcalc):
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")
    return 0
if __name__ == "__main__":
    main()