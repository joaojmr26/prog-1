# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. 
# Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    c1 = a*d
    c2 = (b/100)*5
    total = c1+c2+c
    print( total )
    return 0
if __name__ == "__main__":
    main()