def main():
    soma = 0
    qtd_numeros = 0

    n = int(input())
    while n != 0:
        qtd_numeros += 1
        soma += n
        n = int(input())
    print(f'{soma/qtd_numeros:.2f}')

if __name__ == "__main__":
    main()