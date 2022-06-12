#Função para o tamanho
def f_tam(n):
    cont = 0
    while (n > 0):
        cont += 1
        n = n//10
    return cont

#Função para inverter
def f_inversor(n):
    inv = 0
    tam = f_tam(n) - 1
    while(n > 0):
        a = n % 10
        inv += a * 10**tam
        tam = tam - 1
        n = n // 10
    return inv

# Função para verificar o quadrado perfeito
def f_quad(n):
    d = n
    while (d >= 1):
        if( d * d == n):
            return True
        d = d - 1
    return False

#Função para verificar capicua
def f_cap(n):
    inv = f_inversor(n)
    if (n == inv):
        return True
    else:
        return False

#Função Principal
def main():
    for i in range(1,5001):
        if(f_cap(i) and f_quad(i)):
            print(f'{i} É CAPICUA E QUADRADO PERFEITO ')
        elif(f_cap(i)):
            print(f'{i} É CAPICUA')
        elif(f_quad(i)):
            print(f'{i} É QUADRADO PERFEITO')

    return 0
if __name__ == "__main__":
    main()
