# def main():
#     n = int(input("Numero: "))

#     if eh_impar(n):
#         print("True")
#     else:
#         print("False")

# def eh_impar(n):
#     return n % 2 != 0

# if __name__ == "__main__":
#     main()

# versao runcodes

def main():
    n = int(input())

    if eh_impar(n):
        print("True")
    else:
        print("False")

def eh_impar(n):
    return n % 2 != 0

if __name__ == "__main__":
    main()