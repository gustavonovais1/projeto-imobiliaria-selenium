from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

from selenium.webdriver.chrome.options import Options

url = 'https://www.zukerman.com.br/?gclid=Cj0KCQjw0oyYBhDGARIsAMZEuMt-ti_O4tfxH4f_w_U8_dfg8ZFLW1QfxPYI5ukcDS5ZopB3kjfHb1waAhXuEALw_wcB'

options = Options()
options.headless = True

# Baixando o webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

# Acessando premiro site zukerman
driver.get(url)

# Maximizando a tela
driver.maximize_window()

# Filtrando por estado
estado = Select(driver.find_element(By.ID,'fd-uf'))
estado.select_by_value('go')
sleep(3)

# Feixando baner do sitee
driver.find_element(By.CSS_SELECTOR, 'body > div.fancybox-overlay.fancybox-overlay-fixed > div > div > a').click()

# Clicando no botão de busca
driver.find_element(By.ID, 'btn-fd-ac').click()

listaLinks = []

existePagina = True
primeiraPagina = True

while existePagina == True:
    
    if primeiraPagina:
        primeiraPagina = False
    else:
        try:
            # Clicando no botão de proxima página 
            driver.find_element(By.CSS_SELECTOR, 'body > div.main > div.s-r-m > div.s-it-main > div:nth-child(3) > div.d-pg > ul > li:nth-child(8) > a').click()
        except:
            print("Não existe mais páginas")
            existePagina = False
            driver.close()

    # Extraindo os links para armazenar em listaLinks
    for produtoAtual in driver.find_elements(By.CLASS_NAME, 'cd-it-bt'):
        lista = produtoAtual.find_element(By.TAG_NAME, 'a')
        listaLinks.append(lista.get_attribute('href'))

    for linkAtual in listaLinks:

        # Abrindo links
        driver.get(linkAtual)
        try:
            # Extraindo dados das paginas abetas pelos links
            
            try:
                titulo1 = driver.find_element(By.CLASS_NAME, 's-d-l-m')
                titulo = titulo1.find_element(By.TAG_NAME, 'h1').text
                
                print(titulo)
            except:
                pass

            try:
                endereco = driver.find_element(By.CSS_SELECTOR, 'body > div.main > div.s-d-l-m > div.s-d-l1 > div.s-d-ld > div.s-d-ld-i-main > div.s-d-ld-i2.f-d').text
                print(endereco)
            except:
                print('Por algum motivo não encontramos o endereço, para mais informações acesse: '+ linkAtual)

            try:
                praca1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[2]/div[5]/div/span[2]').text
                print('Premira praça: ' +  praca1)
            except:
                pass

            try:
                # Tentativa de extrair segunda praça 
                praca2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[2]/div[6]/div/span[2]').text
                print('Segunda praça: ' + praca2)
            except:
                pass

            try:
                comitente = driver.find_element(By.CLASS_NAME, 'd-n-v').text
                print('Comitente: ' + comitente)
            except:
                pass

            try:
                lance = driver.find_element(By.CLASS_NAME, 'm-l-o').text
                print('Lance atual: ' + lance)
            except:
                pass

            try:
                # Tratamento de extração para situação do imovél
                situacao = driver.find_elements(By.TAG_NAME, 'p')[1].text
                if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                    print(situacao)
                else:
                    situacao = driver.find_elements(By.TAG_NAME, 'p')[2].text

                    if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                        print(situacao)
                    else:
                        situacao = driver.find_elements(By.TAG_NAME, 'p')[3].text

                        if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                            print(situacao)
                        else:
                            situacao = driver.find_elements(By.TAG_NAME, 'p')[4].text
                            
                            if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                                print(situacao)
                            else:
                                situacao = driver.find_elements(By.TAG_NAME, 'p')[5].text

                                if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                                    print(situacao)
                                else:
                                    situacao = driver.find_elements(By.TAG_NAME, 'p')[6].text

                                    if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                                        print(situacao)
                                    else:
                                        situacao = driver.find_elements(By.TAG_NAME, 'p')[7].text

                                        if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                                            print(situacao)
                                        else:
                                            situacao = driver.find_elements(By.TAG_NAME, 'p')[8].text

                                            if situacao == 'Situação: Imóvel ocupado' or situacao == 'Situação: Imóvel desocupado':
                                                print(situacao)
            except:
                pass

            try:
                # Tratamento de extração para processo do imovél
                processo = driver.find_elements(By.TAG_NAME, 'p')[1].text
                if 'Processo:' in processo :
                    print(processo)
                else:
                    processo = driver.find_elements(By.TAG_NAME, 'p')[2].text

                    if 'Processo:' in processo:
                        print(processo)
                    else:
                        processo = driver.find_elements(By.TAG_NAME, 'p')[3].text

                        if 'Processo:' in processo:
                            print(processo)
                        else:
                            processo = driver.find_elements(By.TAG_NAME, 'p')[4].text
                            
                            if 'Processo:' in processo:
                                print(processo)
                            else:
                                processo = driver.find_elements(By.TAG_NAME, 'p')[5].text

                                if 'Processo:' in processo:
                                    print(processo)
                                else:
                                    processo = driver.find_elements(By.TAG_NAME, 'p')[6].text

                                    if 'Processo:' in processo:
                                        print(processo)
                                    else:
                                        processo = driver.find_elements(By.TAG_NAME, 'p')[7].text

                                        if 'Processo:' in processo:
                                            print(processo)
                                        else:
                                            processo = driver.find_elements(By.TAG_NAME, 'p')[8].text

                                            if 'Processo:' in processo:
                                                print(processo)
                                            else:
                                                processo = driver.find_elements(By.TAG_NAME, 'p')[9].text

                                                if 'Processo:' in processo:
                                                    print(processo)
            except:
                pass


            try:
                # Tratamento de extração para matricula do imovél
                matricula = driver.find_elements(By.TAG_NAME, 'p')[1].text
                if 'Matrícula: ' in matricula :
                    print(matricula)
                else:
                    matricula = driver.find_elements(By.TAG_NAME, 'p')[2].text

                    if 'Matrícula: ' in matricula:
                        print(matricula)
                    else:
                        matricula = driver.find_elements(By.TAG_NAME, 'p')[3].text

                        if 'Matrícula: ' in matricula:
                            print(matricula)
                        else:
                            matricula = driver.find_elements(By.TAG_NAME, 'p')[4].text
                            
                            if 'Matrícula: ' in matricula:
                                print(matricula)
                            else:
                                matricula = driver.find_elements(By.TAG_NAME, 'p')[5].text

                                if 'Matrícula: ' in matricula:
                                    print(matricula)
                                else:
                                    matricula = driver.find_elements(By.TAG_NAME, 'p')[6].text

                                    if 'Matrícula: ' in matricula:
                                        print(matricula)
                                    else:
                                        matricula = driver.find_elements(By.TAG_NAME, 'p')[7].text

                                        if 'Matrícula: ' in matricula:
                                            print(matricula)
                                        else:
                                            matricula = driver.find_elements(By.TAG_NAME, 'p')[8].text

                                            if 'Matrícula: ' in matricula:
                                                print(matricula)
                                            else:
                                                matricula = driver.find_elements(By.TAG_NAME, 'p')[9].text

                                                if 'Matrícula: ' in matricula:
                                                    print(matricula)
            except:
                pass

            try:
                descricao = driver.find_element(By.XPATH, '//*[@id="divdesc"]/div/p').text
                print(descricao)
            except:
                print('Por algum motivo não encontramos a descrição do imovél, para mais informações acesse: '+ linkAtual)

            print('Para mais informações acesse: ' + linkAtual)

        except:
            print("Não foi possível encontrar as informações.")

        print('------------------------------------------------------')

        existePagina = False

# Abrindo nova aba no navegador
driver.execute_script("window.open()")

# Indicando segunda aba para extração
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.megaleiloes.com.br/')

# Clicando no botão de busca avançada
driver.find_element(By.CSS_SELECTOR, '#w16 > li.two-line.full-width.nav-search-nav-menu-item.dropdown > a').click()

# Filtrando por imoveis
categoria = Select(driver.find_element(By.ID, 'search-category'))
categoria.select_by_value('imoveis')
sleep(2)

# Filtrando por estado
estado = Select(driver.find_element(By.NAME, 'estado'))
estado.select_by_value('BA')

# Clicando no botão buscar
driver.find_element(By.ID, 'search-submit').click()

listaLinks = []

existePagina = True
primeiraPagina = True



#dados_page.append(['Titulo', 'Endereço', "Praça1", 'Praça2', 'Comitente', 'Lance' 'Avaliaçâo do imovél', 'Situacao' ,'Processo', 'Descrição', 'Edital', 'Laudo de Avaliação', 'Matricula', 'Link Atual'])


while existePagina == True:
    
    if primeiraPagina:
        primeiraPagina = False
    else:
        try:
            # Clicando no botão para mudar para proxima página
            driver.find_element(By.CSS_SELECTOR, '#w0 > div.text-center > ul > li.next > a').click()
        except:
            print("Não existe mais páginas")
            existePagina = False
            driver.close()

    # Recuperando os links para armazenar em listaLinks
    for produtoAtual in driver.find_elements(By.CLASS_NAME, 'wrap'):
        lista = produtoAtual.find_element(By.TAG_NAME, 'a')
        listaLinks.append(lista.get_attribute('href'))
    
    for linkAtual in listaLinks:

        # Acessando os links
        driver.get(linkAtual)
        try:
            # Extraindo dados das páginas
            titulo = driver.find_element(By.CLASS_NAME, 'section-header').text

            praca1 = driver.find_element(By.CLASS_NAME, 'card-instance-value').text
            data1 = driver.find_element(By.CLASS_NAME, 'card-first-instance-date').text

            lance1 = driver.find_element(By.CLASS_NAME, 'last-bid')
            lance = lance1.find_element(By.CLASS_NAME, 'value').text

            localizacao = driver.find_element(By.CSS_SELECTOR, 'body > div.page > div.container-fluid > div:nth-child(2) > div.col-xs-12.col-sm-6.col-md-8.border > div > div.row > div > div.locality.item > div.value').text

            comitente = driver.find_element(By.CSS_SELECTOR, 'body > div.page > div.container-fluid > div:nth-child(2) > div.col-xs-12.col-sm-6.col-md-8.border > div > div.row > div > div:nth-child(2) > div.value').text

            descricao = driver.find_element(By.CSS_SELECTOR, '#tab-description > div').text

            # Exibindo resultados
            print(titulo)
            print('Endereço: ' + localizacao)
            print('Premeira praça: ' + praca1 + " " + data1)
            try:
                praca2 = driver.find_elements(By.CLASS_NAME, 'card-instance-value')[1].text
                data2 = driver.find_element(By.CLASS_NAME, 'card-second-instance-date').text
                print('Segunda praça: ' + praca2 + " " + data2)
            except:
                pass

            try:
                teste =  driver.find_element(By.CLASS_NAME,'card-second-instance-date')
                testepraca = teste.find_element(By.TAG_NAME, 'b').text

                if testepraca == '3ª Praça:':
                    praca3 = driver.find_elements(By.CLASS_NAME, 'card-instance-value')[2].text
                    data3 = driver.find_elements(By.CLASS_NAME, 'card-second-instance-date')[2].text
                    print('Terceira praça: ' + praca3 + ' ' + data3)
            except:
                pass

            print('Comitente: ' + comitente)
            try:
                processo = driver.find_element(By.CSS_SELECTOR, 'body > div.page > div:nth-child(3) > div:nth-child(2) > div.col-xs-12.col-sm-6.col-md-8.border > div > div > div:nth-child(2) > div.process-number.item > div.value > a').text
                print('Peocesso: ' + processo)
            except:
                pass

            try:
                if lance == 'Faça sua oferta!':
                    print('Lance atual: 0,00')
                else:
                    print('Lance atual: ' + lance)
            except:
                pass

            try:
                # Tratamento de extração para o Edital do imovél
                edital1 = driver.find_element(By.CLASS_NAME, 'downloads')
                edital2 = edital1.find_elements(By.CLASS_NAME, 'btn-download')[0]
                edital3 = edital2.find_element(By.TAG_NAME, 'span').text

                if edital3 == 'Edital' or edital3 == 'Edital Completo':
                    edital1 = driver.find_element(By.CLASS_NAME, 'downloads')
                    edital2 = edital1.find_elements(By.CLASS_NAME, 'btn-download')[0]
                    linkEdital = edital2.get_attribute('href')
                    print('Link do edital: ' + linklinkEdital)
                else:
                    edital1 = driver.find_element(By.CLASS_NAME, 'downloads')
                    edital2 = edital1.find_elements(By.CLASS_NAME, 'btn-download')[1]
                    edital3 = edital2.find_element(By.TAG_NAME, 'span').text

                    if edital3 == 'Edital' or edital3 == 'Edital Completo':
                        edital1 = driver.find_element(By.CLASS_NAME, 'downloads')
                        edital2 = edital1.find_elements(By.CLASS_NAME, 'btn-download')[1]
                        linklinkEdital = edital2.get_attribute('href')
                        print('Link do edital: ' + linklinkEdital)
                    else:
                        edital1 = driver.find_element(By.CLASS_NAME, 'downloads')
                        edital2 = edital1.find_elements(By.CLASS_NAME, 'btn-download')[2]
                        edital3 = edital2.find_element(By.TAG_NAME, 'span').text

                        if edital3 == 'Edital' or edital3 == 'Edital Completo':
                            edital1 = driver.find_element(By.CLASS_NAME, 'downloads')
                            edital2 = edital1.find_elements(By.CLASS_NAME, 'btn-download')[2]
                            linklinkEdital = edital2.get_attribute('href')
                            print('Link do edital: ' + linklinkEdital)
            except:
                pass

            try:
                # Tratamento de extração para o Laudo de Avaliação do imovél
                laudo1 = driver.find_element(By.CLASS_NAME, 'downloads')
                laudo2 = laudo1.find_elements(By.CLASS_NAME, 'btn-download')[0]
                laudo3 = laudo2.find_element(By.TAG_NAME, 'span').text

                if laudo3 == 'Laudo de Avaliação':
                    laudo1 = driver.find_element(By.CLASS_NAME, 'downloads')
                    laudo2 = laudo1.find_elements(By.CLASS_NAME, 'btn-download')[0]
                    linkLaudo = laudo2.get_attribute('href')
                    print('Link laudo de avaliação: ' + linkLaudo)
                else:
                    laudo1 = driver.find_element(By.CLASS_NAME, 'downloads')
                    laudo2 = laudo1.find_elements(By.CLASS_NAME, 'btn-download')[1]
                    laudo3 = laudo2.find_element(By.TAG_NAME, 'span').text

                    if laudo3 == 'Laudo de Avaliação':
                        laudo1 = driver.find_element(By.CLASS_NAME, 'downloads')
                        laudo2 = laudo1.find_elements(By.CLASS_NAME, 'btn-download')[1]
                        linkLaudo = laudo2.get_attribute('href')
                        print('Link laudo de avaliação: ' + linkLaudo)
                    else:
                        laudo1 = driver.find_element(By.CLASS_NAME, 'downloads')
                        laudo2 = laudo1.find_elements(By.CLASS_NAME, 'btn-download')[2]
                        laudo3 = laudo2.find_element(By.TAG_NAME, 'span').text

                        if laudo3 == 'Laudo de Avaliação':
                            laudo1 = driver.find_element(By.CLASS_NAME, 'downloads')
                            laudo2 = laudo1.find_elements(By.CLASS_NAME, 'btn-download')[2]
                            linkLaudo = laudo2.get_attribute('href')
                            print('Link laudo de avaliação: ' + linkLaudo)
            except:
                pass

            try:
                # Tratamento de extração para a matricula do imovél
                matricula1 = driver.find_element(By.CLASS_NAME, 'downloads')
                matricula2 = matricula1.find_elements(By.CLASS_NAME, 'btn-download')[0]
                matricula3 = matricula2.find_element(By.TAG_NAME, 'span').text

                if matricula3 == 'Matricula':
                    matricula1 = driver.find_element(By.CLASS_NAME, 'downloads')
                    matricula2 = matricula1.find_elements(By.CLASS_NAME, 'btn-download')[0]
                    linkMatricula = matricula2.get_attribute('href')
                    print('Link de matricula: ' + linkMatricula)
                else:
                    matricula1 = driver.find_element(By.CLASS_NAME, 'downloads')
                    matricula2 = matricula1.find_elements(By.CLASS_NAME, 'btn-download')[1]
                    matricula3 = matricula2.find_element(By.TAG_NAME, 'span').text

                    if matricula3 == 'Matricula':
                        matricula1 = driver.find_element(By.CLASS_NAME, 'downloads')
                        matricula2 = matricula1.find_elements(By.CLASS_NAME, 'btn-download')[1]
                        linkMatricula = matricula2.get_attribute('href')
                        print('Link de matricula: ' + linkMatricula)
                    else:
                        matricula1 = driver.find_element(By.CLASS_NAME, 'downloads')
                        matricula2 = matricula1.find_elements(By.CLASS_NAME, 'btn-download')[2]
                        matricula3 = matricula2.find_element(By.TAG_NAME, 'span').text

                        if matricula3 == 'Matricula':
                            matricula1 = driver.find_element(By.CLASS_NAME, 'downloads')
                            matricula2 = matricula1.find_elements(By.CLASS_NAME, 'btn-download')[2]
                            linkMatricula = matricula2.get_attribute('href')
                            print('Link de matricula: ' + linkMatricula)
            except:
                pass

            print('Descrição: ' + descricao)

            print('Para mais informações acesse: ' + linkAtual)

            print('-----------------------------------------------------------')
        except:
            print("Não foi possível encontrar as informações.")

        existePagina = False

# Abrindo nova aba
driver.execute_script("window.open()")

# Indicando a terceira aba para extração
driver.switch_to.window(driver.window_handles[2])

# Abrindo terceiro site d1lance
driver.get('https://www.d1lance.com.br/')

# Aceitando cookies da página 
driver.find_element(By.XPATH, '//*[@id="home-pg"]/div[2]/div/button').click()

try:
    # Tentativa de feixar banner do site
    driver.find_element(By.CSS_SELECTOR, '#PopupSignupForm_0 > div.mc-modal > div.mc-closeModal').click()
except:
    pass

# Apetadno no botão de buca avançada 
driver.find_element(By.CSS_SELECTOR, '#header > div.dg-header-nav-box > section.dg-header-nav.dg-naoimprimir > div > div > div.col-xs-12.col-md-9 > div.dg-header-botoes > a.dg-btn.dg-header-buscaavancada.jsBtnBuscaavancada').click()
sleep(2)

# Filtrando por imoveis
cidade = Select(driver.find_element(By.ID,'ID_Categoria'))
cidade.select_by_value('57')

sleep(2)
try:
    # Tentativa de feixar banner do site
    driver.find_element(By.CSS_SELECTOR, '#PopupSignupForm_0 > div.mc-modal > div.mc-closeModal').click()
except:
    pass

sleep(2)
# FIltrando por estado
cidade = Select(driver.find_element(By.ID,'ID_Estado'))

cidade.select_by_value('35')
try:
    # Tentativa de feixar banner do site
    driver.find_element(By.CSS_SELECTOR, '#PopupSignupForm_0 > div.mc-modal > div.mc-closeModal').click()
except:
    pass

sleep(2)

# Clicando no botão de busca
driver.find_element(By.ID, 'btBuscarMenu').click()

listaLinks = []

sleep(3)
while True:

    # Dando scroll na tela até o final
    element = driver.find_element(By.TAG_NAME, 'body')
    element.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(3)
    element.send_keys(Keys.PAGE_DOWN)
    break

existePagina = True
primeiraPagina = False



#dados_page.append(["Titulo", 'Endereço', 'Praca1', 'Praca2','Ctomiente', 'Lance',  'Avaliaçâo do imovél', 'Situacao' , 'Processo',  'Descricao' ,'Edital', 'Laudo de Avaliação', 'Matricula', 'Link Atual'])

sleep(5)

while existePagina == True:

    # Extraindo os links e amarzenando em listaLinks
    for produtoAtual in driver.find_elements(By.CLASS_NAME, "dg-leiloes-acao"):
        lista = produtoAtual.find_element(By.TAG_NAME, 'a')
        listaLinks.append(lista.get_attribute('href'))

    primeiraPagina = False

    if primeiraPagina:
        primeiraPagina = False
    else:
        try:
            # Clicando no botão para mudar para proxima página
            p1 = driver.find_element(By.ID, 'ResultadoPaginacao')
            p2 = p1.find_element(By.CLASS_NAME, 'dg-paginacao')
            p3 = p2.find_element(By.TAG_NAME, 'a').click()
        except:
            print("Não existe mais páginas")
            existePagina = False
            driver.close()

    sleep(5)

    # Dando scroll na tela até o final
    element.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    element.send_keys(Keys.PAGE_DOWN)

    # Extraindo os links e amarzenando em listaLinks
    for produtoAtual in driver.find_elements(By.CLASS_NAME, "dg-leiloes-acao"):
        lista = produtoAtual.find_element(By.TAG_NAME, 'a')
        listaLinks.append(lista.get_attribute('href'))

    existePagina = False

for linkAtual in listaLinks:

    # Acessando os links
    driver.get(linkAtual)

    try:
        # Extraindo e exibindo os dados das páginas

        try:
            titulo = driver.find_elements(By.CLASS_NAME, 'dg-lote-titulo')[0].text
            print(titulo)
        except:
            pass

        try:
            endereco = driver.find_element(By.CLASS_NAME, "dg-lote-local-endereco").text
            print('Endereço: ' + endereco)
        except:
            print('Por algum motivo não encontramos o endereço, para mais informações acesse: '+ linkAtual)

        try:
            sleep(2)
            praca1 = driver.find_element(By.CLASS_NAME, 'ValorMinimoLancePrimeiraPraca').text
            data1 = driver.find_element(By.CLASS_NAME, 'Praca1DataHoraEncerramento').text
            print('Prmeira praça: ' + praca1 + ' ' + data1)
        except:
            pass

        try:
            sleep(1)
            praca2 = driver.find_element(By.CLASS_NAME, 'ValorMinimoLanceSegundaPraca').text
            data2 = driver.find_element(By.CLASS_NAME, 'Praca2DataHoraEncerramento').text
            print('Segunda praça: ' + praca2 + ' ' + data2)
        except:
            pass

        try:
            avaliacaoimovel = driver.find_element(By.CLASS_NAME,'ValorAvaliacao').text
            print('Avaliação do imovél: ' + avaliacaoimovel)
        except:
            pass

        try:
            lance = driver.find_element(By.CLASS_NAME, 'BoxLanceValor').text 
            print('Lance mínimo: ' + lance)
        except:
            pass
                
        print('Ctomiente: Leilão Judicial')

        try: 
            # Tratamento de tentativa de extração da descrição dos imovéis
            descricao = driver.find_element(By.CSS_SELECTOR, '#dg-lote-descricao > div > div.dg-lote-toggle-box > div > p:nth-child(1)').text
            if descricao == 'Casa':
                descricao2 = driver.find_element(By.CSS_SELECTOR, '#dg-lote-descricao > div > div.dg-lote-toggle-box > div > p:nth-child(7) > span > span > span > span:nth-child(2)').text
                print('Descrição: ' + descricao2)
            elif len(descricao) <= 100:
                print('Por algum motivo não encontramos a descrição do imovél, para mais informações acesse: '+ linkAtual)
            else:
                print('Descrição: ' + descricao)
        except:
            try: 

                descricao = driver.find_element(By.CSS_SELECTOR, '#dg-lote-descricao > div > div.dg-lote-toggle-box > div > p:nth-child(1) > span > span > span').text
                if descricao == 'Casa':
                    descricao2 = driver.find_element(By.CSS_SELECTOR, '#dg-lote-descricao > div > div.dg-lote-toggle-box > div > p:nth-child(7) > span > span > span > span:nth-child(2)').text
                    print('Descrição: ' + descricao2)
                elif len(descricao) <= 100:
                    print('Por algum motivo não encontramos a descrição do imovél, para mais informações acesse: '+ linkAtual)
                else:                                                       
                    print('Descrição: ' + descricao)
            except:
                pass

            # Tentativas de extração dos links dos documentos do imovéis 
        try:
            edital1 = driver.find_element(By.CLASS_NAME, 'dg-lote-documentos-downloads')
            link = edital1.find_elements(By.TAG_NAME, 'a')[0]
            edital = link.get_attribute('href')

            print('Link do edital do imovél: ' + edital)
        except:
            pass

        try:
            avaliacao1 = driver.find_element(By.CLASS_NAME, 'dg-lote-documentos-downloads')
            link = avaliacao1.find_elements(By.TAG_NAME, 'a')[3]
            avaliacao = link.get_attribute('href')

            print('Link do laudo de avaliação do imovél: ' + avaliacao)
        except:
            pass

        try:
            matricula1 = driver.find_element(By.CLASS_NAME, 'dg-lote-documentos-downloads')
            link = matricula1.find_elements(By.TAG_NAME, 'a')[2]
            matricula = link.get_attribute('href')

            print('Link do matricula do imovél: ' + matricula)
        except:
            pass
        
        print('Para mais informações acesse: ' + linkAtual)

        print('-------------------------------------------------')
    except:
        print('Não foi possível encontrar as informações.')
