# def main():
#     n = int(input())

#     resto = n
#     c = resto // 100
#     resto %= 100
#     d = resto // 10
#     resto %= 10
#     u = resto

#     qtd_pares = 0
#     if eh_par(c) or c == 0:
#         qtd_pares += 1
#     if eh_par(d) or d == 0:
#         qtd_pares += 1
#     if eh_par(u) or u == 0:
#         qtd_pares += 1

#     print(qtd_pares)

# def eh_par(n):
#     return n % 2 == 0

# if __name__ == "__main__":
#     main()


def main():
    n = input().strip()

    qtd_digitos_pares = 0

    for digito in n:
        if eh_par(int(digito)):
            qtd_digitos_pares += 1

    print(qtd_digitos_pares)

def eh_par(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()