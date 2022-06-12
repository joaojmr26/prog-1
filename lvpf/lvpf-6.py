# Função de cálculo da fatorial

def f_fatorial(n):
    fatorial = 1
    if (n == 0):
        fatorial = 1
    else:
        for i in range (2, n+1):
            fatorial = fatorial*i
    
    return fatorial

#fim da função

# função com o programa principal

def main():
    for a in range(5):
        n = int(input())
        if(n >= 0):
            fatorial = f_fatorial(n)
            print(f'Fatorial({n})={fatorial:.0f}')
    
  

#fim da função main

#invocação/chamada do programa principal

if __name__ == "__main__":

  main()

#fim