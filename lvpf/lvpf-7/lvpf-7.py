import f
def main():
    n = int(input())
    while(n >= 0):
        quadrado = f.f_quadrado(n)
        newton = f.f_newton(quadrado, n)
        print(f'N={n:.4f} RAIZ={newton:.6f}')
        n = int(input())
    

main()