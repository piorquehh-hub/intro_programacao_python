def numero_por_extenso(n):
    unidades = ["zero", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

    partes = []

    resto = n
    c = resto // 100
    resto %= 100
    d = resto // 10
    resto %= 10
    u = resto

    if c > 0:
        if c == 1:
            partes.append("uma centena")
        else:
            partes.append(f"{unidades[c]} centenas")

    if d > 0:
        if d == 1:
            partes.append("uma dezena")
        else:
            partes.append(f"{unidades[d]} dezenas")

    if u > 0:
        if u == 1:
            partes.append("uma unidade")
        else:
            partes.append(f"{unidades[u]} unidades")

    if len(partes) == 1:
        frase = partes[0]
    elif len(partes) == 2:
        frase = " e ".join(partes)
    else:
        frase = f"{partes[0]}, {partes[1]} e {partes[2]}"

    return frase + "."

def main():
    n = int(input())

    if 0 < n < 1000:
        print(f"{n} = {numero_por_extenso(n)}")
    else:
        print("número inválido")

main()