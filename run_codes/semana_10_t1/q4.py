def main():
    sequencia = ""
    for i in range(10, 1010, 10):
        if i == 1000:
            sequencia += str(i) + "."
        else:
            sequencia += str(i) + ", "
    print(sequencia)
if __name__ == "__main__":
    main()