def main():
    numconsumidor = 1
    consr, consc, consi, constotal = int(0), int(0), int(0), int(0)
    maior, menor, cont = int(0), int(1000), int(0)
    valorkwh = float(input())
    while(numconsumidor > 0): #Loop Infinito
        numconsumidor = int(input())
        if(numconsumidor > 0): #Condição de parada
            qntdkwh = int(input())
            codconsumidor = input()
            if(codconsumidor == "R"):
                consr = consr + qntdkwh
            elif(codconsumidor == "C"):
                consc = consc + qntdkwh
            elif(codconsumidor == "I"):
                consi = consi + qntdkwh
            totalpgto = valorkwh * qntdkwh
            print(f'{numconsumidor} {totalpgto:.1f}')
        if(qntdkwh > maior):
            maior = qntdkwh
        if(menor > qntdkwh):
            menor = qntdkwh
        cont = cont + 1 
    cont = cont - 1
    constotal = consr + consc +consi
    media = constotal/cont
    print(f'{maior:.1f}')
    print(f'{menor:.1f}')
    print(f'{consr:.1f}')
    print(f'{consc:.1f}')
    print(f'{consi:.1f}')
    print(f'{media:.1f}')

    return 0
if __name__ == "__main__":
    main()
