def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    dif_b = abs(n1 - n2)
    dif_c = abs(n1 - n3)

    if dif_b < dif_c:
        print(dif_b)
    else:
        print(dif_c)
main()