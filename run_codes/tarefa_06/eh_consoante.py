#versao runcodes
def main():
    char = input().strip().lower()

    if verificar_consoante(char):
        print("True")
    else:
        print("False")

def verificar_consoante(char):
    return char in "bcdfghjklmnpqrstvwxyz"

if __name__ == "__main__":
    main()