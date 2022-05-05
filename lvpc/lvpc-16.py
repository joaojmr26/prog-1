# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. 
# Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, 
# caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas, totalizando o esperado de 160h/mês).

def main():
    h = float(input())
    sh = float(input())
    sm = h*sh
    he = h-160
    if(h>=160):
        she = he*(sh*5/10)
        st = sm+she
        print(st)
    else:
        st = sm
        print(st)
    return 0
if __name__ == "__main__":
    main()