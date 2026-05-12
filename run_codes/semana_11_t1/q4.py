def main():
    # n = input().strip()
    # inverso = ""

    # for i in range(len(n)-1, -1, -1):
    #     inverso += n[i]
    # print(inverso)

    n = int(input())
    inverso = 0

    while n != 0:
        inverso = inverso * 10 + n % 10
        n //= 10
    print(inverso)

if __name__ == "__main__":
    main()