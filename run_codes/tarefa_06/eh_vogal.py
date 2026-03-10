#versao runcodes
def main():
    char = input().strip().lower()

    if verifica_vogal(char):
        print("True")
    else:
        print("False")

def verifica_vogal(char):
    vogais = ["a", "e", "i", "o", "u"]

    return char in vogais

if __name__ == "__main__":
    main()