def main():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    n3 = int(input("Numero 3: "))
    n4 = int(input("Numero 4: "))
    n5 = int(input("Numero 5: "))

    menor = min(n1, n2, n3, n4, n5)
    maior = max(n1, n2, n3, n4, n5)
    media = (n1 + n2 + n3 + n4 + n5) / 5

    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Media: {media}")
    
if __name__ == "__main__":
    main()


# versao runcodes

# def main():
#     n1 = int(input())
#     n2 = int(input())
#     n3 = int(input())
#     n4 = int(input())
#     n5 = int(input())

#     menor = min(n1, n2, n3, n4, n5)
#     maior = max(n1, n2, n3, n4, n5)
#     media = (n1 + n2 + n3 + n4 + n5) / 5

#     print(maior)
#     print(menor)
#     print(media)

# if __name__ == "__main__":
#     main()