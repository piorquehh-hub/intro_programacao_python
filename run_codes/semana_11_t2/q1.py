def main():
    n = int(input())

    soma = 0

    while n != 0:
        soma += n
        n = int(input())
    print(soma)

if __name__ == "__main__":
    main()
