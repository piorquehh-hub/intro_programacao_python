from math import ceil

def main():
    populacao_dodos_inicial = int(input())
    ano_inicial = 1600

    # quantidade de dodos que representa 10% da população inicial
    dodos_10_porcento = populacao_dodos_inicial * 0.1
    tx_nasc = 0.01
    tx_morte = 0.06

    qtd_nascimentos = 0
    qtd_mortes = 0
    total_por_ano = 0

    populacao_dodos = populacao_dodos_inicial

    while populacao_dodos > dodos_10_porcento:
        qtd_nascimentos = ceil(populacao_dodos * tx_nasc)
        qtd_mortes = ceil(populacao_dodos * tx_morte)
        total_por_ano = ceil(qtd_nascimentos - qtd_mortes)

        populacao_dodos += total_por_ano
        print(f"{ano_inicial},{qtd_nascimentos},{qtd_mortes},{populacao_dodos}")
        ano_inicial += 1

if __name__ == "__main__":
    main()