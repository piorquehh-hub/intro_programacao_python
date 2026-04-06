def main():
    mat = input().strip()
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media_exercicios = float(input())

    media_final = (n1 + n2 * 2 + n3 * 3 + media_exercicios) / 7

    if media_final >= 9:
        print(mat)
        print(f"{media_final:.2f}")
        print("A")
        print("Aprovado")
    elif media_final < 9 and media_final >= 7.5:
        print(mat)
        print(f"{media_final:.2f}")
        print("B")
        print("Aprovado")
    elif media_final < 7.5 and media_final >= 6:
        print(mat)
        print(f"{media_final:.2f}")
        print("C")
        print("Aprovado")
    elif media_final < 6 and media_final >= 4:
        print(mat)
        print(f"{media_final:.2f}")
        print("D")
        print("Reprovado")
    elif media_final < 4:
        print(mat)
        print(f"{media_final:.2f}")
        print("E")
        print("Reprovado")
main()