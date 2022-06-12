# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

def main():
    frase = input()
    contb = 0
    conta = 0
    conte = 0
    conti = 0
    conto = 0
    contu = 0
    for i in range(len(frase)):
        if (frase[i] == " "):
            contb += 1
        elif (frase[i] == "A"):
            conta += 1    
        elif (frase[i] == "E"):
            conte += 1 
        elif (frase[i] == "I"):
            conti += 1 
        elif (frase[i] == "O"):
            conto += 1 
        elif (frase[i] == "U"):
            contu += 1 
            
    print("ESPAÇOS EM BRANCO = ", contb)
    print("A = ", conta)
    print("E = ", conte)
    print("i = ", conti)
    print("O = ", conto)
    print("U = ", contu)
    
    return 0
if __name__ == "__main__":
    main()