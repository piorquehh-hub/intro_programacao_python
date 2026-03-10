#versao runcodes
def main():
    valor_lado = float(input())

    area, perimetro = calcular_area_perimetro_quadrado(valor_lado)

    print(f"{area:10.4f}")
    print(f"{perimetro:10.4f}")


def calcular_area_perimetro_quadrado(lado):
    area = lado ** 2
    perimetro = lado * 4

    return area, perimetro


if __name__ == "__main__":
    main()