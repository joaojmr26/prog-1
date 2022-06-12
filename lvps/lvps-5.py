# Modifique o programa anterior (LVP STRINGS 4)  de modo que a escada seja invertida.

def main():
    a = input()
    for i in range(len(a),-1,-1):
        print(a[0:i])
    
if __name__ == "__main__":
    main()