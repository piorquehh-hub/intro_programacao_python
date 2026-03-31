def main():
    n = input().strip()

    qtd_digitos_impares = 0

    for digito in n:
        if not eh_par(int(digito)):
            qtd_digitos_impares += 1

    if qtd_digitos_impares == 0:
        print("Nenhum dígito é ímpar.")
    if qtd_digitos_impares == 1:
        print("Apenas um dígito é ímpar.")
    if qtd_digitos_impares == 2:
        print("Os dois dígitos são ímpares.")

def eh_par(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()