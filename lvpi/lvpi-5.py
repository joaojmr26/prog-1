# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. #

def main():
  a = int(input())
  b = int(input())
  c = int(input())
  dias = (a*365)+(b*30)+c
  print(dias)
  return 0
if __name__ ==  "__main__":
  main()