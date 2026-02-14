# questao 1
print("Pocao do mago")
substancia_1 = float(input("Valor em ml da primeira substancia: "))
substancia_2 = float(input("Valor em ml da segunda substancia: "))

total_pocao = substancia_1 + substancia_2

print(f"Total da pocao: {total_pocao:.2f} ml")

# questao 2
print("Robo catador")
qtd_hrs = int(input("Digite quantas horas o robo vai trabalhar: "))

qtd_pecas = qtd_hrs * 12

print("Quantidade de pecas coletadas: ", qtd_pecas)

# questao 3
print("Poco dos desejos matematicos ???")
valor_encontrado = float(input("Valor encontrado no poco: "))

qtd_moedas_de_vinte_e_cinco = valor_encontrado * 4
 
print(f"Quantidade de moedas de 25 centavos que cabem no valor: {qtd_moedas_de_vinte_e_cinco}")

# questao 4
print("Dragao come ovelha simulator")
qtd_dias_solto = int(input("Quantidade de dias solto: "))

qtd_ovelhas_comidas = qtd_dias_solto / 2

print(f"Dragao comeu {qtd_ovelhas_comidas} ovelha(s)")

# questao 5
print("Dobro, triplo e quadrado!")
x = int(input("x: "))

dobro = x * 2
triplo = x * 3
quadrado = x ** 2

print("Dobro: ", dobro)
print("Triplo: ", triplo)
print("Quadrado: ", quadrado)