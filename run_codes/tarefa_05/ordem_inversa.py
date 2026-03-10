#versao runcodes
def inverte_ordem_do_numero(n):
    milhar = n // 1000
    resto = n % 1000
    centena = resto // 100
    resto %= 100
    dezena = resto // 10
    resto %= 10
    unidade = resto

    return milhar, centena, dezena, unidade

def main():
    n = int(input())

    m, c, d, u = inverte_ordem_do_numero(n)

    print(f"{u}{d}{c}{m}")


if __name__ == "__main__":
    main()