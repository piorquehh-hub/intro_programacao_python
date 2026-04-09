def main():
    # while true para simular um menu
    while True:

        dt_nasc = input("Digite sua data no formato DDMMAAAA: ")

        # validar o input da data previamente
        if not dt_nasc.isdigit() or len(dt_nasc) != 8:
            print("Data inválida!")
            continue

        dt_nasc = int(dt_nasc)

        dia, mes, ano = separar_dt(dt_nasc)
        
        if not valida_data(dia, mes, ano):
            print("Data inválida!")
            continue

        meu_signo = signo(dia, mes)
        horoscopo_hj = horoscopo(meu_signo)

        print(horoscopo_hj)

        continuar = input("\nContinuar? (1-sim / 2-não): ")

        # caso digite opcao invalida o loop encerra
        if continuar not in ['1', '2']:
            print("Opção inválida, encerrando.")
            break
        
        if continuar == '2':
            break


def separar_dt(dma):
    a = dma % 10000
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma
    return d, m, a

# validar a data
def valida_data(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    elif dia < 1 or dia > 31:
        return False
    elif mes in [4, 6, 9, 11] and dia > 30:
        return False
    elif mes == 2:
        if eh_ano_bissexto(ano):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    return True

def eh_ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def signo(dia, mes):
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 21 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'

def remover_acentos(txt):
    from unicodedata import normalize
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def formatar_txt(txt, largura=80):
    import textwrap

    txt = ' '.join(txt.split())

    return textwrap.fill(txt, width=largura)

# usei beatifulsoup por ser mais facil de utilizar
# o codigo original retornava todo o html do site, pois o site foi atualizado.
# o try e except sao para dar mais robustes e feedback 
def horoscopo(signo_desejado):
    import urllib.request
    from bs4 import BeautifulSoup

    ''' copio o signo original pra  exibir certo no output do fim da funcao'''
    signo_original = signo_desejado
    signo_desejado = remover_acentos(signo_desejado).lower()

    url = f'https://www.horoscopovirtual.com.br/horoscopo/{signo_desejado}'

    try:
        req = urllib.request.Request(
            url=url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
        )

        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')

        paragrafos = soup.find_all('p')

        for p in paragrafos:
            texto = p.get_text().strip()

            # verificacao da string retornada para evitar pegar texto incorreto do site
            if (
                len(texto) > 100 and
                'Publicado' not in texto and
                'Atualizado' not in texto and
                'Por' not in texto
            ):
                texto_formatado = formatar_txt(texto)

                # formatando a string para um feedback visual mais acurado
                return f'\n=== {signo_original.upper()} ===\n\n{texto_formatado}\n' 

        return 'Não foi possível encontrar o horóscopo.'

    except Exception as e:
        return f'Erro ao acessar o site: {e}'


if __name__ == '__main__':
    main()