# Faça um programa que receba a idade de uma pessoa, em dias, e apresente a idade dessa pessoa em anos, meses e dias. Considere um ano com 365 dias e um ano com 30 dias.

def main():
    diastotais = int(input())
    a= int(diastotais/365)
    m= int((diastotais % 365)/ 30)
    d= int((diastotais % 365)% 30)
    print (a, m, d)
    return 0
if __name__ == "__main__":
    main()