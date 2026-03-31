# versao runcodes

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    menor = n1
    if (n2 < n1) and (n2 < n3) and (n2 < n4) and (n2 < n5):
        menor = n2
    if (n3 < n1) and (n3 < n2) and (n3 < n4) and (n3 < n5):
        menor = n3
    if (n4 < n1) and (n4 < n2) and (n4 < n3) and (n4 < n5):
        menor = n4
    if (n5 < n1) and (n5 < n2) and (n5 < n3) and (n5 < n4):
        menor = n5

    maior = n1
    if (n2 > n1) and (n2 > n3) and (n2 > n4) and (n2 > n5):
        maior = n2
    if (n3 > n1) and (n3 > n2) and (n3 > n4) and (n3 > n5):
        maior = n3
    if (n4 > n1) and (n4 > n2) and (n4 > n3) and (n4 > n5):
        maior = n4
    if (n5 > n1) and (n5 > n2) and (n5 > n3) and (n5 > n4):
        maior = n5

    print(maior)
    print(menor)

if __name__ == "__main__":
    main()