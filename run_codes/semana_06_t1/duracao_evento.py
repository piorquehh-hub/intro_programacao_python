# def main():
#     duracao_seg = int(input("Digite a duracao em segundos: "))

#     resto = duracao_seg
#     hr = resto // 3600
#     resto %= 3600
#     min = resto // 60
#     resto %= 60

#     print(f"Duracao do evento: {hr}:{min}:{resto}")

# if __name__ == "__main__":
#     main()

# versao runcodes
def main():
    duracao_seg = int(input())

    resto = duracao_seg
    hr = resto // 3600
    resto %= 3600
    min = resto // 60
    resto %= 60

    print(f"{hr}:{min}:{resto}")

if __name__ == "__main__":
    main()