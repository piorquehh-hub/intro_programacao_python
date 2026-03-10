#versao runcodes
def converte_minutos_para_horas_minutos(minutos):
    hr = minutos // 60
    resto = minutos % 60

    return hr, resto

def main():
    min = int(input())

    hr, resto_min = converte_minutos_para_horas_minutos(min)

    print(f"{hr}:{resto_min}")

if __name__ == "__main__":
    main()