def main():
    dia_um = int(input())
    mes_um = int(input())
    ano_um = int(input())

    dia_dois = int(input())
    mes_dois = int(input())
    ano_dois = int(input())

    if (ano_um > ano_dois) or (mes_um > mes_dois) or (dia_um > dia_dois):
        print(f"{dia_um}/{mes_um}/{ano_um}")
    else:
        print(f"{dia_dois}/{mes_dois}/{ano_dois}")

if __name__ == "__main__":
    main()