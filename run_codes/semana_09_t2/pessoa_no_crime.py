def main():
    p1 = input().strip().upper()
    p2 = input().strip().upper()
    p3 = input().strip().upper()
    p4 = input().strip().upper()
    p5 = input().strip().upper()

    qtd_sim = 0

    if p1 == "S":
        qtd_sim += 1

    if p2 == "S":
        qtd_sim += 1
    
    if p3 == "S":
        qtd_sim += 1

    if p4 == "S":
        qtd_sim += 1
    
    if p5 == "S":
        qtd_sim += 1

    if qtd_sim == 2:
        print("Suspeito")
    elif 3 <= qtd_sim <= 4:
        print("Cúmplice")
    elif qtd_sim == 5:
        print("Assassino")
    else:
        print("Inocente")

main()