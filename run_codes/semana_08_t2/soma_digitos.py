def main():
    n = input().strip()
    num = int(n)

    if 0 <= num <= 100000:
        print(sum(int(d) for d in n))
    else:
        print(-1)

main()