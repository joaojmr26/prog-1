# Faça um programa que leia 2 strings e informe se as duas strings 
# possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

def main():
    a = input()
    b = input()
    if(len(a) == len(b)):
        print("MESMO TAMANHO")
    else:
        print("TAMANHO DIFERENTE")
    if(a == b):
        print("CONTEÚDO IGUAL")
    else:
        print("CONTEÚDO DIFERENTE")
    
    return 0
    
if __name__ == "__main__":
    main()