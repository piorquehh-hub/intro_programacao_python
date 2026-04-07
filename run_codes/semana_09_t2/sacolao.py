def main():
    qtd_kg_morango = float(input())
    qtd_kg_maca = float(input())

    valor_kg_morango = 2.50
    valor_kg_maca = 1.80

    if qtd_kg_morango > 5:
        valor_kg_morango = 2.20
    if qtd_kg_maca > 5:
        valor_kg_maca = 1.50

    valor_tt = (qtd_kg_morango * valor_kg_morango) + (qtd_kg_maca * valor_kg_maca)
    kg_tt = qtd_kg_morango + qtd_kg_maca

    if valor_tt > 25 or kg_tt > 8:
        desconto = 0.10 * valor_tt
        valor_tt -= desconto
    
    print(f"{valor_tt:.2f}")

main()