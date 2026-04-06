def main():
    base = int(input())
    altura = int(input())

    if base == altura:
        print("QUADRADO")
    else:
        perimetro = 2 * (base + altura)
        area = base * altura
        print(f"{perimetro} - {area}")
main()