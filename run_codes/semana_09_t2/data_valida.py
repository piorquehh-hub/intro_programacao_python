def main():
    dt = input().strip()

    dia = dt[0:2]
    mes = dt[2:4]
    ano = dt[4:8]

    dia_int = int(dia)
    mes_int = int(mes)
    ano_int = int(ano)

    valida = True

    if mes_int < 1 or mes_int > 12:
        valida = False
    elif dia_int < 1 or dia_int > 31:
        valida = False
    elif mes_int in [4, 6, 9, 11] and dia_int > 30:
        valida = False
    elif mes_int == 2:
        if eh_ano_bissexto(ano_int):
            if dia_int > 29:
                valida = False
        else:
            if dia_int > 28:
                valida = False

    if valida:
        print("True")
    else:
        print("False")


def eh_ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


main()