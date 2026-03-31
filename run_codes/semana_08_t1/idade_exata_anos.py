# versao runcodes

def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())

    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())

    idade = ano_atual - ano_nasc

    if (mes_atual < mes_nasc) or (mes_atual == mes_nasc and dia_atual < dia_nasc):
        idade -= 1

    print(idade)

if __name__ == "__main__":
    main()