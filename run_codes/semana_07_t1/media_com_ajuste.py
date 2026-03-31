def main():
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    n3 = float(input("Numero 3: "))

    media = (n1 + n2 + n3) / 3

    if n3 > 8:
        media += 1

        if media > 10:
            media = 10
    
    print(media)

if __name__ == "__main__":
    main()

# versao runcodes

# def main():
#     n1 = float(input())
#     n2 = float(input())
#     n3 = float(input())

#     media = (n1 + n2 + n3) / 3

#     if n3 > 8:
#         media += 1

#         if media > 10:
#             media = 10

#     print(media)

# if __name__ == "__main__":
#     main()