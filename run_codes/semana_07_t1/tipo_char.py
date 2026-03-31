def main():
    char = input("Letra: ").lower()

    if eh_vogal(char):
        print("vogal")
    elif eh_consoante(char):
        print("consoante")
    elif eh_numero(char):
        print("número")
    else:
        print("símbolo")
    

def eh_vogal(char):
    return char in "aeiou"

def eh_consoante(char):
    return char in "bcdfghjklmnpqrstvwxyz"

def eh_numero(char):
    return char.isnumeric()

if __name__ == "__main__":
    main()

# versao runcodes

# def main():
#     char = input().lower()

#     if eh_vogal(char):
#         print("vogal")
#     elif eh_consoante(char):
#         print("consoante")
#     elif eh_numero(char):
#         print("número")
#     else:
#         print("símbolo")

# def eh_vogal(char):
#     return char in "aeiou"

# def eh_consoante(char):
#     return char in "bcdfghjklmnpqrstvwxyz"

# def eh_numero(char):
#     return char.isnumeric()

# if __name__ == "__main__":
#     main()