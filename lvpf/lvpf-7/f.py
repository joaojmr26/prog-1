def f_quadrado(n):
    raiz = n**(1/2)
    int(round(raiz))
    quadrado = raiz
    return(quadrado)

def f_newton(quadrado, n):
    valor = quadrado**2
    newton = ((n+valor)/(2*quadrado))
    return(newton)
