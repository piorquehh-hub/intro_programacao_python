#versao runcodes
def main():
    char = input()

    if verificar_simbolo(char):
        print("True")
    else:
        print("False")

def verificar_simbolo(char):
    return not char.isalnum()

if __name__ == "__main__":
    main()