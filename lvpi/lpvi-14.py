# Faça um programa que recebe dois pares de coordenadas e calcule a distância entre os pontos. 

def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    dis = (((x2-x1)**2) + ((y2-y1)**2))**0.5
    print (dis)
    return 0
if __name__ == "__main__":
    main()