def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    qtd_iguais = 0

    if n1 == n2:
        qtd_iguais += 1
    if n2 == n3:
        qtd_iguais += 1
    if n1 == n3:
        qtd_iguais += 1

    if qtd_iguais == 0:
        print("Todos os valores são diferentes")
    elif qtd_iguais == 1:
        print("Existem dois valores iguais e um diferente")
    elif qtd_iguais == 3:
        print("Todos os valores são iguais.")

main()