def main():
    qtd_pares = 0
    qtd_impares = 0

    for i in range(100):
        num = int(input())

        if eh_par(num):
            qtd_pares += 1
        else:
            qtd_impares += 1

    print(f"{qtd_pares}")
    print(f"{qtd_impares}")

def eh_par(num):
    return num % 2 == 0

if __name__ == "__main__":
    main()