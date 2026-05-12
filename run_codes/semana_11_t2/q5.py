def main():
    while True:
        nota = float(input())

        if nota < 0 or nota > 10:
            print('Nota inválida.')
        else:
            if nota >= 8.5:
                print('A')
            elif 7 <= nota < 8.5:
                print('B')
            elif 5 <= nota < 7:
                print('C')
            elif 4 <= nota < 5:
                print('D')
            else:
                print('E')
            break

if __name__ == "__main__":
    main()