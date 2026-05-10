def main():
    valor_medio = 0
    for i in range(100):
        n = int(input())
        valor_medio += n
    valor_medio /= 100
    print(f"{valor_medio:.2f}")

if __name__ == "__main__":
    main()