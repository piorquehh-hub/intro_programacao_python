def main():
    n = int(input())

    resto = n % 5

    if resto == 0:
        resultado = 9 * n + 7
        print(resultado)

    elif resto == 1:
        if n % 2 == 0:
            print("par")
        else:
            print("ímpar")

    elif resto == 2:
        resultado = 5 * (n ** 2) - 3 * n + 42
        print(resultado)

    elif resto == 3:
        print(n // 10)

    elif resto == 4:
        print(n ** 2)

main()