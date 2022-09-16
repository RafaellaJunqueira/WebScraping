import time
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def search_name(**in_args):
    user_input = in_args['name']
    # Opção para headless Chrome. Para tirar o headless, é só remover o argumento 'options' do driver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options=chrome_options)

    # Opção para headless Firefox. Para tirar o headless, é só remover o argumento 'options' do driver
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)

    driver.get('https://portal.stf.jus.br/')
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, '//option[@value="PARTE_OU_ADVOGADO"]').click()
    driver.find_element(By.ID, 'pesquisaPrincipalParteAdvogado').send_keys(user_input)
    driver.find_element(By.ID, 'btnPesquisar').click()
    sleep(3)
    
    # Extracao com Beautiful Soup
    html_page = driver.page_source
    soup = BeautifulSoup(html_page, 'lxml')
    result_table = soup.find('table')
    headers = result_table.find_all('th')
    lines = result_table.select('tr:not(:first-child)')
    
    result_list = list()
    for line in lines:
        temp_dict = dict()
        cells = line.find_all('td')
        for index, cell in enumerate(cells):
            if cell.text != '':
                temp_dict[headers[index].text] = cell.text
        result_list.append(temp_dict.copy())

    # print(f'RESULTADO: {result_list}')
    driver.quit()


if __name__ == '__main__':
    start = time.time()
    args = {"name": "Vitor Borges"}
    search_name(**args)
    end = time.time()
    print(f'TEMPO DE EXECUÇÃO:{end - start}')