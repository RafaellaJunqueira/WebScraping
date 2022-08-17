import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def search_name(**in_args):
    user_input = in_args['name']
    driver = webdriver.Chrome()
    driver.get('https://portal.stf.jus.br/')
    driver.find_element(By.XPATH, '//option[@value="PARTE_OU_ADVOGADO"]').click()
    driver.find_element(By.ID, 'pesquisaPrincipalParteAdvogado').send_keys(user_input)
    driver.find_element(By.ID, 'btnPesquisar').click()
    driver.refresh()
    result_table = driver.find_element(By.TAG_NAME, 'table')
    headers = result_table.find_elements(By.TAG_NAME, 'th')
    lines = result_table.find_elements(By.CSS_SELECTOR, 'tr:not(:first-child)')

    result_list = list()
    for line in lines:
        temp_dict = dict()
        cells = line.find_elements(By.TAG_NAME, 'td')
        for index, cell in enumerate(cells):
            if cell.text != '':
                temp_dict[headers[index].text] = cell.text
        result_list.append(temp_dict.copy())

    print(result_list)

if __name__ == '__main__':
    args = {"name": "Vitor Borges"}
    search_name(**args)