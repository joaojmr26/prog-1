# Tendo como dados de entrada a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas: - para sexo masculino: peso ideal = (72.7 * altura) - 58 – para sexo feminino: peso ideal = (62.1 * altura) - 44.7

def main():
    s = input().upper()
    a = float(input())
    if(s == "M"):
        p = (72.7 * a) - 58
        print(p)
    else:
        p = (62.1 * a) - 44.7
        print(p)
    return 0
if __name__ == "__main__":
    main()