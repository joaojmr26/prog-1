# Função Conversão Para Binario
def f_binario(n):
    n_bin = str
    n_bin = bin(n)
    return(n_bin)

#Função Conversão Para Hex
def f_hex(n):
    n_hex = str
    n_hex = hex(n)
    return(n_hex)

#Função Principal
def main():
    n = int(input())
    while(n > 0):
        n_bin = f_binario(n)[2:]
        n_hex = f_hex(n)[2:].upper()
        print(f'DEC={n} BIN={n_bin} HEX={n_hex}')
        n = int(input())
    return 0

if __name__ == "__main__":
    main()
