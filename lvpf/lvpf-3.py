# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento  negativo ou 'Z' se for zero.

def f_arg(arg):
    if(arg>0):
        return("P")
    elif(arg<0):
        return("N")
    else:
        return("Z")
    
def main():
    arg = int(input())
    s = f_arg(arg)
    print(s)
    return 0

if __name__ == "__main__":
    main()
