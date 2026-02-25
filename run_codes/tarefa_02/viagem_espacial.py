## versao normal

distancia = int(input("Digite a distância em km: "))
velocidade = int(input("Digite a velocidade média em km/h: "))

hrs_viagem = distancia / velocidade
dias_viagem = hrs_viagem / 24
resto = hrs_viagem % 24

print(f"Uma viagem de {distancia} km vai levar {int(dias_viagem)} dia(s) e {hrs_viagem} hora(s).")