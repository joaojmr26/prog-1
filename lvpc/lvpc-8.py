# Leia o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu). 
# Considere o ano atual como 2021 e a idade mínima, para votar, 16 anos.

def main():
    a = int(input())
    voto = 2021-a
    if voto>=18:
        print("PODE VOTAR")
    else:
        print("NÃO PODE VOTAR")
    return 0
if __name__ == "__main__":
    main()