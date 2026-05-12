def main():
    deposito_inicial = float(input())
    taxa_juros_anual = float(input())

    valor_acumulado = deposito_inicial
    qtd_anos = 0
    while valor_acumulado < 2 * deposito_inicial:
        valor_acumulado += valor_acumulado * (taxa_juros_anual / 100)
        qtd_anos += 1
    print(f'{qtd_anos}')

if __name__ == "__main__":
    main()