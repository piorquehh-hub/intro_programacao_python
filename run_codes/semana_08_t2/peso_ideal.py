def main():
    altura = float(input("Altura: "))
    sexo = int(input("Sexo 1-macho / 2-feme: "))

    imc = 0
    if sexo == 1:
        imc = 72.7 * altura - 58
    elif sexo == 2:
        imc = 62.1 * altura - 44.7

    print(f"{imc:.2f}")

main()