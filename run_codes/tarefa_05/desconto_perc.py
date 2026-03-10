#versao runcodes

def main():
    valor = float(input())
    valor_percentual = float(input())

    percentual_calculado = calcular_percentual(valor, valor_percentual)

    valor_com_aumento = calcular_aumento(valor, percentual_calculado)
    valor_com_desconto = calcular_desconto(valor, percentual_calculado)

    print(f"{valor_com_aumento:.2f}")
    print(f"{valor_com_desconto:.2f}")

def calcular_percentual(valor, valor_percentual):
    return valor * (valor_percentual / 100)

def calcular_aumento(valor, valor_aumento):
    return valor + valor_aumento

def calcular_desconto(valor, valor_desconto):
    return valor - valor_desconto


if __name__ == "__main__":
    main()