#versao runcodes
def main():
    char = input()

    if verificar_letra_numero(char):
        print("True")
    else:
        print("False")

def verificar_letra_numero(char):
    return char.isalnum()

if __name__ == "__main__":
    main()