# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Alcool:
# Até 20 litros, desconto de 3%
# Acima 20 litros, desconto de 5%

# Gasolina:
# Até 20 litros, desconto de 4%
# Acima 20 litros, desconto de 6%

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool ou  G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90

def main():
    g = 3.30
    a = 2.90
    litros = float(input())
    tipo = input().upper()
    if (tipo =="A"):
        bomba = litros*a
        if(litros <= 20):
            valor = bomba - (bomba*3/100)
        else:
            valor = bomba - (bomba*5/100)
    else:
        if (tipo == "G" and litros <= 20):
            bomba = litros*g
            valor = bomba - (bomba*4/100)
        else:
            bomba = litros*g
            valor = bomba - (bomba*6/100)
    print(f'{valor:.2f}')
    return 0
if __name__ == "__main__":
    main()