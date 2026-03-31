def main():
    valor_compra = float(input("Valor da compra: "))

    desconto_nove_porcento = valor_compra * 0.09
    juros_dezessete_porcento = valor_compra * 0.17

    valor_avista = valor_compra - desconto_nove_porcento
    prestacao_cinco_vezes = valor_compra / 5
    prestacao_dez_vezes = (valor_compra + juros_dezessete_porcento) / 10

    print(f"Valor a vista: R$ {valor_avista:.2f}")
    print(f"Valor da prestacao se parcelado em 5x: R$ {prestacao_cinco_vezes:.2f}")
    print(f"Valor da prestacao se parcelado em 10x: R$ {prestacao_dez_vezes:.2f}")

if __name__ == "__main__":
    main()

# versao runcodes

# def main():
#     valor_compra = float(input())

#     desconto_nove_porcento = valor_compra * 0.09
#     juros_dezessete_porcento = valor_compra * 0.17

#     valor_avista = valor_compra - desconto_nove_porcento
#     prestacao_cinco_vezes = valor_compra / 5
#     prestacao_dez_vezes = (valor_compra + juros_dezessete_porcento) / 10

#     print(f"{valor_avista:.2f}")
#     print(f"{prestacao_cinco_vezes:.2f}")
#     print(f"{prestacao_dez_vezes:.2f}")

# if __name__ == "__main__":
#     main()