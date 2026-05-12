def main():
    valor_tt = 0    
    while True:
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')

        codigo = input().strip().upper()[0]

        if codigo == "X":
            print(f'{valor_tt:.2f}')
            break
        elif codigo == "H":
            valor_tt += 5.50
        elif codigo == "C":
            valor_tt += 6.80
        elif codigo == "M":
            valor_tt += 4.50
        elif codigo == "A":
            valor_tt += 7
        elif codigo == "Q":
            valor_tt += 4
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()