#versao runcodes
def main():
    char = input().strip().lower()

    if verifica_char(char):
        print("True")
    else:
        print("False")


def verifica_char(char):
    return char in "abcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":
    main()