def main():
    n = int(input())
    maior = n
    menor = n

    while n != 0:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        n = int(input())
    print(f'{maior}\n{menor}')

if __name__ == "__main__":
    main()