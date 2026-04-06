def main():
    n1 = int(input())
    n2 = int(input())
    opcao = int(input())

    if opcao == 1:
        print(n1 + n2)
    elif opcao == 2:
        print(n1 - n2)
    elif opcao == 3:
        print(n1 * n2)
    elif opcao == 4:
        print(n1 / n2)

main()