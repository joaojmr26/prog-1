# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
# Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'NÃO EFETUAR COMPRA', senão escrever a mensagem 'EFETUAR COMPRA'.

def main():
    qa = int(input())
    qm = int(input())
    qmin = int(input())
    qmed = ((qm + qmin)/2)
    if(qa>=qmed):
        print("NÃO EFETUAR COMPRA")
    else:
        print("EFETUAR COMPRA")
    return 0
if __name__ == "__main__":
    main()