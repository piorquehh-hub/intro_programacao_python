def main():
    tx_natalidade_a = 0.02
    tx_natalidade_b = 0.03

    pop_1 = int(input())
    pop_2 = int(input())

    # ordenando as populações para facilitar o processo de comparação
    # o pais A tem a maior população
    if pop_1 > pop_2:
        pop_a = pop_1
        pop_b = pop_2
    else:
        pop_a = pop_2
        pop_b = pop_1

    anos = 0
    while pop_a > pop_b:
        pop_a += int(pop_a * tx_natalidade_a)
        pop_b += int(pop_b * tx_natalidade_b)
        anos += 1
    print(anos)

if __name__ == "__main__":
    main()