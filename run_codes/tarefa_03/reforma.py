# versao runcodes

# altura = float(input())
# comprimento = float(input())
# largura = float(input())
# 
# area_piso = largura * comprimento
# volume_sala = largura * comprimento * altura
# area_parede_sala = (2 * altura) * largura + (2 * altura) * comprimento
# 
# print(area_piso)
# print(volume_sala)
# print(area_parede_sala)


## versao normal

altura = float(input("Digite a altura da sala: "))
comprimento = float(input("Digite o comprimento da sala: "))
largura = float(input("Digite a largura da sala: "))

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_parede_sala = (2 * altura) * largura + (2 * altura) * comprimento

print("Área do piso:", area_piso)
print("Volume da sala:", volume_sala)
print("Área das paredes da sala:", area_parede_sala)