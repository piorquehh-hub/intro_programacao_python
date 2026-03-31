def main():
    nome = input("Nome: ")
    estado_civil = int(input("Estado civil (1 - cassado / 2 - solteiro): "))

    qtd_char_nomes = len(nome)
    if estado_civil == 1:
        nome_conjuge = input("Nome do conmjuge: ")
        qtd_char_nomes += len(nome_conjuge)
    
    print(f"Quantidade de caracteres nos nomes lidos: ")

if __name__ == "__main__":
    main()

# versao runcodes

# def main():
#     nome = input().strip()
#     estado_civil = int(input())

#     qtd_char_nomes = len(nome)
#     if estado_civil == 1:
#         nome_conjuge = input().strip()
#         qtd_char_nomes = len(nome + nome_conjuge)
    
#     print(qtd_char_nomes)

# if __name__ == "__main__":
#     main()