def main():
    while True:
        print("OPÇÕES: \n1 - SAUDAÇÃO \n2 - BRONCA \n3 - FELICITAÇÃO \n0 - FIM")
        n = int(input())
        if n == 0:
            print("0 - Fim de serviço.")
            break
        elif n == 1:
            print("1 - Olá. Como vai?")
        elif n == 2:
            print("2 - Vamos estudar mais.")
        elif n == 3:
            print("3 - Meus Parabéns!")
        else:
            print("Opção inválida.")     

if __name__ == "__main__":
    main()