def main():
    qtd_pessoas = 0
    soma_idades = 0
    maior_idade = 0
    menor_idade = 0

    while True:
        n = int(input())
        if n == 0:
            break

        qtd_pessoas += 1
        soma_idades += n
        if n > maior_idade:
            maior_idade = n
        if menor_idade == 0 or n < menor_idade:
            menor_idade = n
    print(f'{qtd_pessoas}\n{soma_idades/qtd_pessoas:.2f}\n{menor_idade}\n{maior_idade}')

if __name__ == "__main__":
    main()
        