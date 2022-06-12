# Modifique o programa anterior (LVP STRINGS 3) de forma a mostrar o nome em formato de escada.

def main():
    a = input()
    for i in range(len(a)):
        print(a[0:i+1])
    
if __name__ == "__main__":
    main()