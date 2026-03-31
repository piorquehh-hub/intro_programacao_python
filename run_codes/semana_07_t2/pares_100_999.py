def main():
    n = input().strip()

    qtd_digitos_pares = 0

    for digito in n:
        if eh_par(int(digito)):
            qtd_digitos_pares += 1

    print(qtd_digitos_pares)

def eh_par(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()