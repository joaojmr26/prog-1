def main():
    #Declaração de Variaveis:
    media_a, media_b, media_c, media_d = int(0), int(0), int(0), int(0)
    qntd_a, qntd_b, qntd_c, qntd_d, qntd_taus, maior, menor = int(0), int(0), int(0), int(0), int(0), int(0), int(0)
    qntd_aus, qntd_pres, nturmas,= int(0), int(0), int(0)
    idturma = str()
    qntdalunos = int()
    mtrclalunos = str()
    frqalunos = str()
    nturmas = int(input())
    for n in range(nturmas):
        #Entrada de dados
        idturma = str(input())
        qntdalunos = int(input())

        while(idturma == "turmaA"):
            #Inicialização e Entrada de variáveis
            qntd_a = qntdalunos
            for i in range (qntd_a):
                mtrclalunos = str(input())
                frqalunos = str(input())
                #Processamento
                if( frqalunos == "A" ):
                    qntd_aus += 1
                else:
                    qntd_pres += 1
            media_a = ((100*qntd_aus)/(qntd_aus+qntd_pres))
            qntd_aus, qntd_pres, qntdalunos = 0, 0, 0
            idturma = ""
            if( media_a > 20):
                qntd_taus += 1

        while(idturma == "turmaB"):
            #Inicialização e Entrada de variáveis
            qntd_b = qntdalunos
            for i in range (qntd_b):
                mtrclalunos = str(input())
                frqalunos = str(input())
                #Processamento
                if( frqalunos == "A" ):
                    qntd_taus += 1
                else:
                    qntd_pres += 1
            media_b = ((100*qntd_aus)/(qntd_aus+qntd_pres))
            qntd_aus, qntd_pres, qntdalunos = 0, 0, 0
            idturma = ""
            if( media_b > 20):
                qntd_taus += 1

        while(idturma == "turmaC"):
            #Inicialização e Entrada de variáveis
            qntd_c = qntdalunos
            for i in range (qntd_c):
                mtrclalunos = str(input())
                frqalunos = str(input())
                #Processamento
                if( frqalunos == "A" ):
                    qntd_aus += 1
                else:
                    qntd_pres += 1
            media_c = ((100*qntd_aus)/(qntd_aus+qntd_pres))
            qntd_aus, qntd_pres, qntdalunos = 0, 0, 0
            idturma = ""
            if( media_c > 20):
                qntd_taus += 1

        while(idturma == "turmaD"):
            #Inicialização e Entrada de variáveis
            qntd_d = qntdalunos
            for i in range (qntd_d):
                mtrclalunos = str(input())
                frqalunos = str(input())
                #Processamento
                if( frqalunos == "A" ):
                    qntd_aus += 1
                else:
                    qntd_pres += 1
            media_d = ((100*qntd_aus)/(qntd_aus+qntd_pres))
            qntd_aus, qntd_pres, qntdalunos = 0, 0, 0
            idturma = ""
            if( media_d > 20):
                qntd_taus += 1

        #Inicialização de variáveis        
        maior = qntd_a
        menor = qntd_a

    #Processamento

    if(media_b > maior ):
        maior = media_b
    if (media_c > maior):
        maior = media_c
    if(media_d > maior):
        maior = media_d
    if(media_b < menor ):
        menor = media_b
    if (media_c < menor):
        menor = media_c
    if(media_d < menor):
        menor = media_d
        
    #Saída de dados

    print(f'TURMA= turmaA AUSENCIA= {media_a:.2f} %')
    print(f'TURMA= turmaB AUSENCIA= {media_b:.2f} %')
    print(f'TURMA= turmaC AUSENCIA= {media_c:.2f} %')
    print(f'TURMA= turmaD AUSENCIA= {media_d:.2f} %')
    print(f'TURMA COM MAIOR % DE AUSENCIA= turmaC AUSENCIA= {maior:.2f} %')
    print(f'TURMA COM MENOR % DE AUSENCIA= turmaB AUSENCIA= {menor:.2f} %')
    print(f'{qntd_taus} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')


            


if __name__ == "__main__":
    main()