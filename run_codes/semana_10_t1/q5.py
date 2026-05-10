def main():
    maior = 0
    for i in range(100):
        n = int(input())
        if n > maior:
            maior = n
    print(f"{maior}")   

if __name__ == "__main__":
    main()