def main():
    valor_da_compra = float(input())

    for i in range(1, 25):
        if i > 0:
            print(f'{i}x de R$ {valor_da_compra / i:.2f}')

if __name__ == "__main__":
    main()