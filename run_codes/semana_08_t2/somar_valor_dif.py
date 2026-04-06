def main():
    n = int(input())

    if eh_par(n):
        n += 5
    else:
        n += 8

    print(n)

def eh_par(n):
    return n % 2 == 0

main()