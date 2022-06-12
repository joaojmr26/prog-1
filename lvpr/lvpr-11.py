# Faça um Programa que leia números até que o usuário não queira mais digitar os números. 
# No final escrever a soma dos valores positivos e a soma dos valores negativos.  
# (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)

def main():
    somap = 0
    soman = 0
    cont = 0
    r = str(input( ))
    while (r.upper() == "S"):
        n = int(input( ))
        if (n > 0):
            somap = somap + n
        else:
            soman = soman + n
        r = input( )
        
    print(somap, soman)
    return 0
    
if __name__ == "__main__":
    main()