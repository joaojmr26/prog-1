# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

def main():
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    dn = input()
    d = int(dn[0:2])
    m = int(dn[3:5])
    a = int(dn[6:])
    mes = m-1
    print(d, "de", meses[mes], "de", a)

    
    return 0
if __name__ == "__main__":
    main()