# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores. #

def main():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  base = a/100
  brancos = b/base 
  nulos = c/base
  validos = d/base
  print( "BRANCOS=", brancos, "%")
  print( "NULOS=", nulos, "%")
  print( "VALIDOS=", validos, "%")
  return 0
if __name__ ==  "__main__":
  main()