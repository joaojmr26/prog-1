# Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

def main():
    s = float(input())
    v = float(input())
    if(v<=1500):
        st = s + (v*3/100)
        print(st)
    else:
        st = s + (1500*(3/100)) + ((v-1500)*(5/100))
        print(st)
    return 0
if __name__ == "__main__":
    main()